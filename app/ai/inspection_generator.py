import json

from app.ai.openai_service import client
from app.ai.prompts import INSPECTION_REPORT_PROMPT
from app.schemas.inspection import InspectionResponse


def generate_inspection_report(data):
    prompt = INSPECTION_REPORT_PROMPT.format(
        inspection_type=data.inspection_type,
        occupancy_type=data.occupancy_type,
        notes="\n".join(data.inspector_notes)
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert fire inspection AI assistant. "
                    "Return ONLY valid JSON with this exact structure: "
                    "{inspection_summary: string, findings: array of objects. "
                    "Each finding must include issue, location, severity, "
                    "description, corrective_action, and code_reference.}"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()
    content = content.replace("```json", "").replace("```", "").strip()

    parsed = json.loads(content)

    validated = InspectionResponse(**parsed)

    return validated.model_dump()

def generate_combined_inspection_report(data):

    notes_text = "\n".join(data.inspector_notes)

    photo_findings_text = ""

    for finding in data.photo_findings:
        photo_findings_text += f"""
Photo Finding:
Issue: {finding.issue}
Location: {finding.location}
Severity: {finding.severity}
Description: {finding.description}
Corrective Action: {finding.corrective_action}
Code Reference: {finding.code_reference}
"""

    combined_prompt = f"""
You are an expert fire inspection AI assistant.

Create one unified fire inspection report using both written inspector notes and photo-based findings.

Inspection Type:
{data.inspection_type}

Occupancy Type:
{data.occupancy_type}

Inspector Notes:
{notes_text}

Photo Findings:
{photo_findings_text}

Return ONLY valid JSON with this exact structure:
{{
  "inspection_summary": "string",
  "findings": [
    {{
      "issue": "string",
      "location": "string",
      "severity": "Low, Medium, or High",
      "description": "string",
      "corrective_action": "string",
      "code_reference": "string"
    }}
  ]
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert fire inspection AI assistant. "
                    "Return ONLY valid JSON. Do not use markdown."
                )
            },
            {
                "role": "user",
                "content": combined_prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()
    content = content.replace("```json", "").replace("```", "").strip()

    parsed = json.loads(content)

    validated = InspectionResponse(**parsed)

    return validated.model_dump()