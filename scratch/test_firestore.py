
import asyncio
import os
from google.cloud import firestore

# To test with emulator: export FIRESTORE_EMULATOR_HOST="localhost:8080"

async def test_firestore():
    db = firestore.AsyncClient()
    print("Connecting to Firestore...")
    
    # Add a test document
    doc_ref = db.collection("requests").document("test_doc")
    await doc_ref.set({
        "user_id": 0,
        "user_email": "test@example.com",
        "query": "Hello Firestore!",
        "timestamp": firestore.SERVER_TIMESTAMP
    })
    print("Document added.")
    
    # Read it back
    doc = await doc_ref.get()
    if doc.exists:
        print(f"Document found: {doc.to_dict()}")
    else:
        print("Document NOT found.")

if __name__ == "__main__":
    asyncio.run(test_firestore())
