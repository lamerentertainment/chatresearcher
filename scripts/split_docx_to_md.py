import zipfile
import xml.etree.ElementTree as ET
import sys
import os
import re

def extract_raw_text(docx_path):
    document_xml = 'word/document.xml'
    try:
        with zipfile.ZipFile(docx_path) as docx:
            xml_content = docx.read(document_xml)
        
        root = ET.fromstring(xml_content)
        namespaces = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
        }
        
        paragraphs = []
        for p in root.findall('.//w:p', namespaces):
            parts = []
            for t in p.findall('.//w:t', namespaces):
                if t.text:
                    parts.append(t.text)
            if parts:
                paragraphs.append(" ".join(parts))
                
        return "\n".join(paragraphs)
    except Exception as e:
        print(f"Error reading docx: {e}")
        return ""

def split_and_save(text, output_dir):
    output_tb_dir = os.path.join(output_dir, 'tb')
    if not os.path.exists(output_tb_dir):
        os.makedirs(output_tb_dir)

    # Use a more flexible pattern for the blocks
    # Looking for #Beginn [header]# [content] #Ende [footer]#
    # We use a non-greedy .*? for content to avoid eating up multiple blocks
    pattern = re.compile(r'#\s*Beginn\s+(.*?)\s*#(.*?)#\s*Ende\s+(.*?)\s*#', re.DOTALL | re.IGNORECASE)
    
    matches = list(pattern.finditer(text))
    print(f"Found {len(matches)} blocks.")
    
    indices = []
    for i, match in enumerate(matches):
        header = match.group(1).strip()
        content = match.group(2).strip()
        footer = match.group(3).strip()
        
        # Parse header to extract ID and Title
        # Standard format: [ID] [Title]
        # Example IDs: StGB11, StGB 163, SVG92a
        header_parts = header.split()
        if not header_parts:
            continue
            
        # Try to identify the ID (usually first word, or first two if first is StGB/StPO/SVG/etc)
        if len(header_parts) > 1 and header_parts[0].lower() in ['stgb', 'stpo', 'svg', 'aig', 'betmg']:
            # If the second word starts with a digit, it's likely part of the ID
            if header_parts[1][0].isdigit():
                clean_id = f"{header_parts[0]}{header_parts[1]}"
                title = " ".join(header_parts[2:])
            else:
                clean_id = header_parts[0]
                title = " ".join(header_parts[1:])
        else:
            clean_id = header_parts[0]
            title = " ".join(header_parts[1:])
            
        # Add to index list
        indices.append((clean_id, title))

        # Standardize content: extract date if nearby
        end_pos = match.end()
        next_pos = matches[i+1].start() if i+1 < len(matches) else len(text)
        tail = text[end_pos:next_pos]
        
        # Flexible date regex (handles 28.03.2026 or 6.2.23)
        date_match = re.search(r'hinzugefügt am\s+(\d{1,2}\.\d{1,2}\.[\d]{2,4})', tail, re.IGNORECASE)
        date_str = date_match.group(0) if date_match else ""
        
        # Build the final chunk text
        chunk_content = f"{clean_id}\t{title}\n\n"
        chunk_content += f"#Beginn {clean_id} {title}#{content}#Ende {clean_id}#\n\n"
        if date_str:
            chunk_content += f"{date_str}\n"

        filename = f"{clean_id}.md"
        filename = re.sub(r'[^\w\-_\.]', '_', filename)
        
        file_path = os.path.join(output_tb_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(chunk_content)

    # Write index.md
    if indices:
        indices.sort() # Sort by ID
        index_content = "# Index der Textbausteine\n\n"
        index_content += "| Kürzel | Titel | Datei |\n"
        index_content += "| :--- | :--- | :--- |\n"
        for cid, t in indices:
            fname = re.sub(r'[^\w\-_\.]', '_', cid) + ".md"
            index_content += f"| {cid} | {t} | [{fname}]({fname}) |\n"
        
        index_path = os.path.join(output_tb_dir, "index.md")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print(f"Index created with {len(indices)} entries.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 split_docx_to_md.py <docx_file> <output_directory>")
        sys.exit(1)
        
    docx_file = sys.argv[1]
    output_directory = sys.argv[2]
    
    raw_text = extract_raw_text(docx_file)
    if raw_text:
        split_and_save(raw_text, output_directory)
        print("Done.")
    else:
        print("No text extracted.")
