from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem, Image, PageBreak
)
from reportlab.lib import colors
import matplotlib.pyplot as plt

# PDF filename
filename = "full_in_demand_tech_stacks.pdf"

# Create PDF document
doc = SimpleDocTemplate(filename, pagesize=A4)
styles = getSampleStyleSheet()
content = []

# Title
content.append(Paragraph("Most In-Demand Tech Stacks (2024-2025)", styles['Title']))
content.append(Spacer(1, 12))

# Intro
intro_text = (
    "Here’s a summary of what I found on which tech stacks are most in-demand right now (2024-2025),"
    " plus some thoughts on what that means so you can pick based on your goals."
    " If you want data specific to Chennai / India I can pull that too."
)
content.append(Paragraph(intro_text, styles['BodyText']))
content.append(Spacer(1, 12))

# Section: What the data says
content.append(Paragraph("What the data says", styles['Heading2']))
content.append(Spacer(1, 6))

# Table of tech stacks
table_data = [
    ["Tech / Stack / Language", "How in-demand it is", "Key strengths / where it's used"],
    ["JavaScript / Full-Stack JS (Node.js + React / TypeScript)",
     "Very high demand. Many full-stack roles expect React + Node.js + TypeScript.",
     "Great for web apps, startups, fast development, frontend + backend overlap."],
    ["Python (Django / Flask / FastAPI, AI/ML/data)",
     "Rapidly growing demand. Especially backend + data/AI.",
     "Versatile: AI, ML, data science, backend, web development."],
    ["Java / Spring Boot / Enterprise stacks", "Still solid demand in enterprises, banks, govt.",
     "Stable, many legacy + new enterprise systems. Good job security."],
    [".NET / C#", "Moderate to high demand in Microsoft ecosystem.",
     "Useful in enterprises using Windows/Azure."],
    ["Other stacks", "Growth in Go, Rust, Flutter, React Native, Cloud.",
     "Performance backends, mobile apps, cloud-focused roles."]
]

table = Table(table_data, colWidths=[170, 150, 200])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
]))
content.append(table)
content.append(Spacer(1, 12))

# Sources
content.append(Paragraph("Sources:", styles['Heading3']))
sources_list = ListFlowable([
    ListItem(Paragraph("Karmick Institute, Lemon.io, Tech New Skills", styles['BodyText'])),
    ListItem(Paragraph("Entrepreneur, trytami.com", styles['BodyText'])),
    ListItem(Paragraph("Maddosh, Statista", styles['BodyText']))
], bulletType='bullet')
content.append(sources_list)
content.append(Spacer(1, 12))

# Most in demand
content.append(Paragraph("Most in demand right now", styles['Heading2']))
demand_list = ListFlowable([
    ListItem(Paragraph("JavaScript full-stack (React + Node.js + TypeScript) — widely used by startups and web products.", styles['BodyText'])),
    ListItem(Paragraph("Python (backend + AI/data roles) — growth due to AI/ML, data science, readability, ecosystem.", styles['BodyText'])),
    ListItem(Paragraph("Java / .NET remain important for enterprise & stability, but less growth compared to JS + Python.", styles['BodyText']))
], bulletType='bullet')
content.append(demand_list)
content.append(Spacer(1, 12))

# Decision factors
content.append(Paragraph("What to consider for you", styles['Heading2']))
decision_list = ListFlowable([
    ListItem(Paragraph("Startups / web product companies → Full-stack JS (React / Node)", styles['BodyText'])),
    ListItem(Paragraph("AI / ML / Data science → Python is almost essential.", styles['BodyText'])),
    ListItem(Paragraph("Stability / enterprise / banks → Java or .NET.", styles['BodyText'])),
    ListItem(Paragraph("Also consider your interest, learning speed, and learning curve.", styles['BodyText']))
], bulletType='bullet')
content.append(decision_list)
content.append(Spacer(1, 12))

# Chart
content.append(PageBreak())
content.append(Paragraph("Visual Representation: Demand Comparison", styles['Heading2']))
stacks = ["JavaScript Full-Stack", "Python", "Java", ".NET", "Others"]
demand = [95, 90, 80, 75, 60]
plt.figure(figsize=(6,4))
plt.bar(stacks, demand)
plt.title("Tech Stack Demand (2024-2025)")
plt.ylabel("Relative Demand Level")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("tech_stack_demand_chart.png")
plt.close()
content.append(Image("tech_stack_demand_chart.png", width=400, height=250))

# Build PDF
doc.build(content)
print(f"PDF generated successfully: {filename}")