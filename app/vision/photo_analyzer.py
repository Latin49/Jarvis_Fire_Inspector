import base64
import json

from app.ai.openai_service import client


def analyze_inspection_photo(image_bytes, filename):

    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert fire inspection photo analysis assistant. "
                    "Analyze inspection photos for visible fire and life safety issues. "
                    "Return ONLY valid JSON."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Analyze this fire inspection photo. "
                            "Identify visible hazards, possible code concerns, "
                            "severity, recommended corrective actions, and confidence level. "
                            "Return JSON with this structure: "
                            "{photo_filename, summary, findings:[{issue, severity, description, corrective_action, confidence}]}"
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()
    content = content.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(content)
    except Exception as e:
        return {
            "photo_filename": filename,
            "summary": "Unable to parse AI vision response.",
            "error": str(e),
            "raw": content
        }