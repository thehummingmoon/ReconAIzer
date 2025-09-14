from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def generate_pdf_report(data, filename):
    """Generates a PDF report from the collected data."""
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Title
    title_style = ParagraphStyle('TitleStyle', parent=styles['Normal'], fontSize=24, spaceAfter=20, alignment=TA_CENTER)
    story.append(Paragraph("Reconnaissance Report", title_style))
    story.append(Paragraph(f"Target: {data['Target']}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Add a paragraph for each section
    for section_title, section_data in data.items():
        if section_title == "Target":
            continue
        
        story.append(Paragraph(f"<b><u>{section_title}</u></b>", styles['Heading2']))
        if isinstance(section_data, dict):
            for key, value in section_data.items():
                story.append(Paragraph(f"<b>{key}:</b>", styles['Normal']))
                if isinstance(value, list):
                    for item in value:
                        story.append(Paragraph(f"- {item}", styles['Normal']))
                else:
                    story.append(Paragraph(str(value), styles['Normal']))
                story.append(Spacer(1, 6))
        else:
            story.append(Paragraph(str(section_data), styles['Normal']))
        story.append(Spacer(1, 12))

    doc.build(story)