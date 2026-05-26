from pydantic import BaseModel
from typing import List


class InspectionRequest(BaseModel):
    occupancy_type: str
    inspection_type: str
    inspector_notes: List[str]


class Finding(BaseModel):
    issue: str
    location: str
    severity: str
    description: str
    corrective_action: str
    code_reference: str


class InspectionResponse(BaseModel):
    inspection_summary: str
    findings: List[Finding]
    
class CombinedInspectionRequest(BaseModel):
    occupancy_type: str
    inspection_type: str
    inspector_notes: List[str]
    photo_findings: List[Finding] = []