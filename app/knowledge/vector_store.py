import chromadb


client = chromadb.PersistentClient(
    path="data/chroma_db"
)


collection = client.get_or_create_collection(
    name="jarvis_fire_code"
)


def add_chunks_to_vector_store(chunks, embeddings, source_name: str):

    for index, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            embeddings=[embeddings[index].tolist()],
            metadatas=[
                {
                    "source": source_name,
                    "chunk_index": index
                }
            ],
            ids=[
                f"{source_name}_{index}"
            ]
        )


def search_vector_store(query_embedding, results_count: int = 5):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=results_count
    )

    return results