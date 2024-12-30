from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import wikipediaapi

user_agent = "MyApp/1.0 (https:myapp.example.com; myemail@example.com) Wikipedia-API/5.0"

wiki_wiki = wikipediaapi.Wikipedia(user_agent)


def fetch_wikipedia_page(page_title):
    page = wiki_wiki.page(page_title)
    if (page.exists()):
        return page.text
    else:
        print(f"The Page '{page_title}' does not exist")
        return None


page_title = "Java (programming language)"
page_content = fetch_wikipedia_page(page_title)

if page_content:
    documents = [page_content]
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


    query = "What is Java?"
    similar_docs = find_all_similar(query, vectorizer, vector_store, documents, 1)

    for doc in similar_docs:
        print(f"Documents:{doc[0][:200]}, Similarity Score: {doc[1]:4f}")
