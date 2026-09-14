import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from database.mongodb import collection

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_documents():
    """
    Mengambil seluruh data Common Information
    dari MongoDB.
    """

    documents = list(collection.find({}, {"_id": 0}))

    return documents


def retrieve_information(query, top_k=3):
    """
    Mencari informasi yang paling relevan
    berdasarkan pertanyaan user.
    """

    documents = get_documents()

    if not documents:
        return []

    texts = [
        f"{doc['category']} {doc['question']} {doc['answer']}"
        for doc in documents
    ]

    vectorizer = TfidfVectorizer()

    document_vectors = vectorizer.fit_transform(texts)
    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    ).flatten()

    ranked_indices = similarities.argsort()[::-1][:top_k]

    results = []

    for index in ranked_indices:
        results.append({
            "category": documents[index]["category"],
            "question": documents[index]["question"],
            "answer": documents[index]["answer"],
            "score": round(float(similarities[index]), 4)
        })

    return results


if __name__ == "__main__":

    query = input("Masukkan pertanyaan: ")

    results = retrieve_information(query)

    print("\nHasil Retrieval:\n")

    for result in results:
        print(f"Category : {result['category']}")
        print(f"Question : {result['question']}")
        print(f"Answer   : {result['answer']}")
        print(f"Score    : {result['score']}")
        print("-" * 50)