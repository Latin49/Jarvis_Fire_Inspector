from embeddings import model
from vector_store import search_vector_store


def retrieve_relevant_chunks(
    query: str,
    results_count: int = 5
):

    query_embedding = model.encode(query)

    results = search_vector_store(
        query_embedding=query_embedding,
        results_count=results_count
    )

    return results