from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

documents = [
    "An exception handler is code designed to handle errors or exceptional conditions during program execution.",
    "Exceptions are unexpected events that disrupt the normal flow of a program, like invalid inputs or division by zero.",
    "The try block contains code that might throw an exception.",
    "The catch (or except) block handles the exception if it occurs.",
    "The finally block is optional and contains code that executes regardless of whether an exception occurred, often used for cleanup.",
    "Raise or throw is used to explicitly trigger an exception in the program.",
    "Exception handling helps in isolating error-prone code from the rest of the program.",
    "It improves code readability by separating normal logic from error-handling logic.",
    "Exception handling prevents abrupt program termination and ensures graceful recovery.",
    "It ensures proper resource management, like closing files or database connections."
]

vectorizer = TfidfVectorizer()
vector_store = vectorizer.fit_transform(documents)

def find_all_similar(query, vectorizer, vector_store, documents, top_k=None):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, vector_store).flatten()
    sorted_indices = np.argsort(similarities)[::-1]

    if top_k is not None:
        sorted_indices = sorted_indices[:top_k]

    similar_docs = [(documents[i], similarities[i]) for i in sorted_indices]

    return similar_docs



query = "throw"
similar_docs = find_all_similar(query, vectorizer, vector_store, documents, 2)

for doc in similar_docs:
    print(f"Documents:{doc[0]}, Similarity Score: {doc[1]:4f}")
