from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime

# Create PDF
pdf_path = "APPROACH.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                        rightMargin=0.5*inch, leftMargin=0.5*inch,
                        topMargin=0.5*inch, bottomMargin=0.5*inch)

# Container for the 'Flowable' objects
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#003366'),
    spaceAfter=30,
    alignment=1  # Center
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#003366'),
    spaceAfter=12,
    spaceBefore=12
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=11,
    spaceAfter=10
)

# Title Page
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("TalentLens AI", title_style))
elements.append(Paragraph("Candidate Ranking System", title_style))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph("An AI-Powered Approach to Smarter Hiring", heading_style))
elements.append(Spacer(1, 1*inch))
elements.append(Paragraph(f"<b>Generated:</b> {datetime.now().strftime('%B %d, %Y')}", body_style))
elements.append(PageBreak())

# Problem Statement
elements.append(Paragraph("1. Problem Statement", heading_style))
elements.append(Paragraph(
    "Recruiters review hundreds of candidate profiles and often miss highly relevant candidates for specialized AI/ML roles. "
    "Traditional keyword-based filtering overlooks candidates with deep technical depth, non-obvious title matches, and diverse career paths that map to the job requirements.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph(
    "<b>The Challenge:</b> How can we rank candidates the way a great recruiter would—by understanding who truly fits the role, not just matching keywords?",
    body_style
))
elements.append(Spacer(1, 0.3*inch))

# Solution Approach
elements.append(Paragraph("2. Solution Approach", heading_style))
elements.append(Paragraph(
    "TalentLens AI uses a <b>hybrid semantic + rule-based ranking system</b> that combines traditional talent signals "
    "with modern AI embeddings to evaluate candidate fit holistically.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# Hybrid Ranking Framework
elements.append(Paragraph("Hybrid Ranking Framework", ParagraphStyle(
    'SubHeading',
    parent=styles['Heading3'],
    fontSize=12,
    textColor=colors.HexColor('#003366'),
)))
elements.append(Spacer(1, 0.1*inch))

data = [
    ['Component', 'Weight', 'Purpose'],
    ['Rule-Based Scoring', '40%', 'Title, experience, skills, career history, recruiter signals'],
    ['Semantic Embeddings', '60%', 'Deep understanding of job description and candidate profile alignment']
]
table = Table(data, colWidths=[2*inch, 1.2*inch, 2.6*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#003366')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
elements.append(table)
elements.append(Spacer(1, 0.3*inch))

# Scoring Components
elements.append(Paragraph("3. Scoring Components", heading_style))

components_text = """
<b>A. Rule-Based Signals (40% weight):</b><br/>
• <b>Job Title Matching:</b> AI-aligned roles (+40), disqualifying roles (-60)<br/>
• <b>Experience Range:</b> 5-9 years target (+25), 4-11 years acceptable (+15)<br/>
• <b>Technical Skills:</b> Embeddings, retrieval, ranking, vector databases (+5 per match)<br/>
• <b>Career History:</b> Search engineer (+30), Recommendation systems (+35), ML roles (+25)<br/>
• <b>Recruiter Signals:</b> Response rate, open-to-work status, search activity<br/>
<br/>
<b>B. Semantic Matching (60% weight):</b><br/>
• Uses Sentence-Transformer embeddings (all-MiniLM-L6-v2 model)<br/>
• Embeds job description and candidate profiles into vector space<br/>
• Calculates cosine similarity for semantic relevance<br/>
• Captures nuanced role requirements beyond keyword matching<br/>
"""
elements.append(Paragraph(components_text, body_style))
elements.append(PageBreak())

# Algorithm
elements.append(Paragraph("4. Ranking Algorithm", heading_style))

algo_text = """
<b>For each candidate:</b><br/>
<br/>
1. <u>Rule-Based Score (S_rule)</u>:<br/>
   • Evaluate title, experience, skills, history, and recruiter signals<br/>
   • Sum weighted scores across all matching criteria<br/>
   <br/>
2. <u>Semantic Score (S_semantic)</u>:<br/>
   • Embed job description: <font color="blue">embedding(job_description)</font><br/>
   • Embed candidate profile: <font color="blue">embedding(profile + skills + history)</font><br/>
   • Calculate similarity: <font color="blue">cos_similarity(jd_embed, candidate_embed) × 100</font><br/>
   <br/>
3. <u>Final Hybrid Score</u>:<br/>
   • <font color="blue">Final Score = (S_rule × 0.4) + (S_semantic × 0.6)</font><br/>
   <br/>
4. <u>Ranking</u>:<br/>
   • Sort candidates by Final Score in descending order<br/>
   • Output top 100 ranked candidates to submission.csv<br/>
"""
elements.append(Paragraph(algo_text, body_style))
elements.append(Spacer(1, 0.2*inch))

# Data Pipeline
elements.append(Paragraph("5. Data Pipeline", heading_style))
pipeline_text = """
<b>Input:</b> Candidate data (candidates.jsonl) + Job description (job_description.docx)<br/>
<b>Processing:</b> Python ranking engine with embeddings and hybrid scoring<br/>
<b>Output:</b> Ranked candidates (submission.csv) with scores<br/>
<b>Visualization:</b> React dashboard for shortlist review and search<br/>
"""
elements.append(Paragraph(pipeline_text, body_style))
elements.append(PageBreak())

# Output Format
elements.append(Paragraph("6. Output Format", heading_style))
elements.append(Paragraph(
    "The submission.csv file contains ranked candidates in CSV format:",
    body_style
))
elements.append(Spacer(1, 0.1*inch))

csv_data = [
    ['candidate_id', 'rank', 'score'],
    ['CAND_0018499', '1', '539.00'],
    ['CAND_0092278', '2', '502.00'],
    ['CAND_0033861', '3', '474.00'],
    ['...', '...', '...']
]
csv_table = Table(csv_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
csv_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#003366')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
elements.append(csv_table)
elements.append(Spacer(1, 0.3*inch))

# Key Advantages
elements.append(Paragraph("7. Key Advantages", heading_style))
advantages_text = """
<b>Over Traditional Keyword Matching:</b><br/>
✓ Understands job requirements holistically, not just keywords<br/>
✓ Captures relevant experience even with non-standard titles<br/>
✓ Combines structured rules with semantic understanding<br/>
✓ Leverages recruiter signals (response rate, availability)<br/>
✓ Prioritizes production experience and demonstrated impact<br/>
✓ Transparent scoring (rule-based + semantic) for insights<br/>
"""
elements.append(Paragraph(advantages_text, body_style))
elements.append(PageBreak())

# Getting Started
elements.append(Paragraph("8. How to Run", heading_style))
getting_started_text = """
<b>Backend (Generate Ranked Output):</b><br/>
<font color="blue">cd ai-candidate-ranker/Backend/src<br/>
python rank_candidates.py</font><br/>
<br/>
<b>Copy Output to Frontend:</b><br/>
<font color="blue">cp output/submission.csv ai-candidate-ranker/Frontend/public/submission.csv</font><br/>
<br/>
<b>Start Frontend Dashboard:</b><br/>
<font color="blue">cd c:\\Users\\acer\\OneDrive\\Desktop\\AI_Candidate_Ranker\\ai-candidate-ranker<br/>
npm run preview</font><br/>
<br/>
<b>View Results:</b><br/>
Open the displayed localhost URL in your browser to explore ranked candidates.<br/>
"""
elements.append(Paragraph(getting_started_text, body_style))
elements.append(Spacer(1, 0.3*inch))

# Summary
elements.append(Paragraph("9. Summary", heading_style))
summary_text = """
TalentLens AI combines the best of both worlds: the structured, interpretable rules that capture domain knowledge about AI/ML hiring, 
and the power of modern semantic embeddings to understand nuanced fit. The hybrid approach ensures both precision (catching role-specific requirements) 
and recall (finding candidates with non-obvious but relevant backgrounds).
"""
elements.append(Paragraph(summary_text, body_style))

# Build PDF
doc.build(elements)
print(f"PDF deck generated: {pdf_path}")
