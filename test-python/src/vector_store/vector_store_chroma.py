import chromadb
client = chromadb.Client()

collection = client.create_collection("all-my-documents")

collection.add(
    documents=["My Name is Dhananjaya", "Dhananjaya is a Software Engineer"],
    metadatas=[{"source": "notion"}, {"source": "google-docs"}],
    ids=["doc1", "doc2"],
)

results = collection.query(
    query_texts=["Who is Dhananjaya"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)

print(results)
# print(results['documents'][0][0])
