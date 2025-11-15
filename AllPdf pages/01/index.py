from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

# Create PDF
pdf_file = "/mnt/data/poshan_vatika_poster.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4)

# Styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(name="TitleStyle", fontSize=28, alignment=TA_CENTER, textColor="green", spaceAfter=20)
subtitle_style = ParagraphStyle(name="SubtitleStyle", fontSize=18, alignment=TA_CENTER, textColor="darkgreen", italic=True, spaceAfter=20)
tagline_style = ParagraphStyle(name="TaglineStyle", fontSize=16, alignment=TA_CENTER, textColor="brown", spaceAfter=30)
author_style = ParagraphStyle(name="AuthorStyle", fontSize=14, alignment=TA_CENTER, textColor="black")

# Content
content = []

# Add top image (garden/healthy food illustration placeholder)
top_img = Image("https://cdn.pixabay.com/photo/2017/06/02/18/24/vegetables-2362615_1280.jpg", width=400, height=200)
top_img.hAlign = "CENTER"
content.append(top_img)
content.append(Spacer(1, 20))

# Title
content.append(Paragraph("🌿 POSHAN VATIKA 🌿", title_style))
content.append(Paragraph("Nutrition from Our Own Garden", subtitle_style))

# Tagline
content.append(Paragraph("🍎 Healthy Food, Healthy Life 🍇", tagline_style))

# Add bottom image (basket of fruits/vegetables)
bottom_img = Image("https://cdn.pixabay.com/photo/2014/04/10/11/24/vegetables-320136_1280.jpg", width=350, height=180)
bottom_img.hAlign = "CENTER"
content.append(bottom_img)
content.append(Spacer(1, 20))

# Author
content.append(Paragraph("— By: Ajay Thakur", author_style))

# Build PDF
doc.build(content)

pdf_file
