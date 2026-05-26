from knowledge.document_loader import load_pdf_text
from knowledge.chunker import chunk_text
from knowledge.embeddings import create_embeddings
from knowledge.vector_store import (
    add_chunks_to_vector_store
)


def ingest_pdf(file_path: str, source_name: str):

    print(f"Loading PDF: {source_name}")

    text = load_pdf_text(file_path)

    print("Chunking text...")

    chunks = chunk_text(text)

    print(f"Created {len(chunks)} chunks")

    print("Generating embeddings...")

    embeddings = create_embeddings(chunks)

    print("Saving to vector database...")

    add_chunks_to_vector_store(
        chunks,
        embeddings,
        source_name
    )

    print("Ingestion complete.")