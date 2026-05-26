from knowledge.rag_pipeline import ingest_pdf


pdf_files = [
    {
        "file_path": "data/2022FireCodeReg_T19_24.pdf",
        "source_name": "2022_CFC"
    },
    {
        "file_path": "data/18-006_large_family_day_care_classified_i4_occupancy.pdf",
        "source_name": "CFM18-006"
    },
    {
        "file_path": "data/24012_childcare_centers_occup_class_use.pdf",
        "source_name": "Updated code24012"
    }
]


print("Starting multi-PDF ingestion...")

for pdf in pdf_files:
    print(f"Ingesting: {pdf['source_name']}")

    ingest_pdf(
        file_path=pdf["file_path"],
        source_name=pdf["source_name"]
    )

print("All PDFs ingested.")