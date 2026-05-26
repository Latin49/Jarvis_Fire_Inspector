from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

from datetime import datetime


def generate_pdf_report(report_data, filename="inspection_report.pdf"):

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Jarvis Fire Inspection Report",
        styles['Title']
    )

    elements.append(title)
    elements.append(Spacer(1, 20))

    date_text = Paragraph(
        f"Generated: {datetime.now()}",
        styles['Normal']
    )

    elements.append(date_text)
    elements.append(Spacer(1, 20))

    summary = Paragraph(
        f"<b>Inspection Summary:</b><br/>{report_data['inspection_summary']}",
        styles['BodyText']
    )

    elements.append(summary)
    elements.append(Spacer(1, 20))

    findings_title = Paragraph(
        "<b>Inspection Findings</b>",
        styles['Heading2']
    )

    elements.append(findings_title)
    elements.append(Spacer(1, 12))

    for finding in report_data["findings"]:

        finding_text = f"""
        <b>Issue:</b> {finding['issue']}<br/>
        <b>Location:</b> {finding['location']}<br/>
        <b>Severity:</b> {finding['severity']}<br/>
        <b>Description:</b> {finding['description']}<br/>
        <b>Corrective Action:</b> {finding['corrective_action']}<br/>
        <b>Code Reference:</b> {finding['code_reference']}<br/>
        """

        paragraph = Paragraph(
            finding_text,
            styles['BodyText']
        )

        elements.append(paragraph)
        elements.append(Spacer(1, 18))

    doc.build(elements)

    return filename