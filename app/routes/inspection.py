from fastapi import APIRouter

from app.schemas.inspection import InspectionRequest
from app.ai.inspection_generator import (
    generate_inspection_report,
    generate_combined_inspection_report
)

from app.schemas.inspection import CombinedInspectionRequest

router = APIRouter()

from fastapi import UploadFile, File

from app.vision.photo_analyzer import analyze_inspection_photo

from fastapi.responses import FileResponse

from app.reports.pdf_generator import generate_pdf_report

from app.schemas.inspection import CombinedInspectionRequest

@router.post("/inspection-report")
def create_inspection_report(data: InspectionRequest):
    return generate_inspection_report(data)
@router.post("/inspection-report")
def create_inspection_report(data: InspectionRequest):
    return generate_inspection_report(data)
@router.post("/generate-pdf")
def create_pdf_report(data: InspectionRequest):

    report = generate_inspection_report(data)

    pdf_file = generate_pdf_report(report)

    return FileResponse(
        path=pdf_file,
        filename=pdf_file,
        media_type='application/pdf'
    )
@router.post("/analyze-photo")
async def analyze_photo(file: UploadFile = File(...)):

    image_bytes = await file.read()

    result = analyze_inspection_photo(
        image_bytes=image_bytes,
        filename=file.filename
    )

    return result

@router.post("/combined-generate-pdf")
def create_combined_pdf_report(
    data: CombinedInspectionRequest
):

    report = generate_combined_inspection_report(data)

    pdf_file = generate_pdf_report(report)

    return FileResponse(
        path=pdf_file,
        filename=pdf_file,
        media_type='application/pdf'
    )