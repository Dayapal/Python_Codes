from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors

# Output file
quiz_pdf = "JS_Interview_Quiz.pdf"
doc = SimpleDocTemplate(quiz_pdf, pagesize=A4)

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="MyTitle", fontSize=22, alignment=TA_CENTER,
                          textColor=colors.darkblue, spaceAfter=20))
styles.add(ParagraphStyle(name="MyHeader", fontSize=16, alignment=TA_LEFT,
                          textColor=colors.white, backColor=colors.darkblue,
                          spaceBefore=10, spaceAfter=10, leading=18, leftIndent=5))
styles.add(ParagraphStyle(name="MyQuestion", fontSize=11, alignment=TA_LEFT,
                          textColor=colors.darkblue, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name="MyOption", fontSize=10, alignment=TA_LEFT,
                          textColor=colors.black, leftIndent=20, leading=12))
styles.add(ParagraphStyle(name="MyAnswer", fontSize=11, alignment=TA_LEFT,
                          textColor=colors.green, leading=14, spaceAfter=12, leftIndent=10))
styles.add(ParagraphStyle(name="SummaryHeader", fontSize=14, alignment=TA_CENTER,
                          textColor=colors.white, backColor=colors.green, spaceAfter=10))

# Content
content = []

# Title Page
content.append(Paragraph("📘 JavaScript Interview Quiz (20 Questions)", styles["MyTitle"]))
content.append(Spacer(1, 20))
content.append(Paragraph(
    "This quiz covers **JavaScript basics, variables, and data types**.<br/>"
    "Each question has four options (A–D).<br/>"
    "👉 The **Answer Key** is provided at the end.",
    styles["MyQuestion"]
))
content.append(PageBreak())

# Questions
questions = [
    ("What is JavaScript primarily used for?", 
     ["Making web pages interactive", "Server hardware programming", "Operating system design", "Database queries"], "A"),
    ("Which company created JavaScript?", 
     ["Microsoft", "Sun Microsystems", "Netscape", "Oracle"], "C"),
    ("Which keyword is used to declare a variable in modern JS?", 
     ["int", "let", "define", "var"], "B"),
    ("What is the difference between let and const?", 
     ["No difference", "const is block-scoped", "let can’t be reassigned", "const can’t be reassigned"], "D"),
    ("What will `typeof null` return?", 
     ["null", "undefined", "object", "error"], "C"),
    ("Which of the following is NOT a primitive data type?", 
     ["String", "Object", "Number", "Boolean"], "B"),
    ("What does `undefined` mean in JavaScript?", 
     ["Variable declared but not assigned", "A null value", "An error", "A type of object"], "A"),
    ("Which of these can store multiple values in JS?", 
     ["Boolean", "Array", "Number", "String"], "B"),
    ("What is a symbol in JavaScript?", 
     ["Emoji", "Unique identifier", "Error type", "Number"], "B"),
    ("Which of the following is correct for declaring a constant?", 
     ["let pi = 3.14;", "var pi = 3.14;", "const pi = 3.14;", "define pi = 3.14;"], "C"),
    ("What will `console.log(5 + '5')` output?", 
     ["10", "55", "Error", "undefined"], "B"),
    ("What is the default value of an uninitialized variable?", 
     ["null", "0", "undefined", "false"], "C"),
    ("Which data type is used for true/false values?", 
     ["Boolean", "String", "Number", "Bit"], "A"),
    ("Which operator checks both value and type?", 
     ["==", "===", "!=", "="], "B"),
    ("Which keyword is block-scoped?", 
     ["var", "let", "static", "def"], "B"),
    ("What will `typeof NaN` return?", 
     ["undefined", "NaN", "number", "error"], "C"),
    ("Which is used for very large integers?", 
     ["float", "BigInt", "Number", "double"], "B"),
    ("Which data type represents an ordered collection?", 
     ["Object", "Function", "Array", "Symbol"], "C"),
    ("What is the output of `typeof undefined`?", 
     ["object", "undefined", "null", "error"], "B"),
    ("Why do we use variables?", 
     ["To store data", "To loop", "To create servers", "To debug code"], "A")
]

# Add Questions
for i, (q, opts, ans) in enumerate(questions, 1):
    content.append(Paragraph(f"Q{i}. {q}", styles["MyQuestion"]))
    for j, opt in zip(["A", "B", "C", "D"], opts):
        content.append(Paragraph(f"{j}. {opt}", styles["MyOption"]))
    content.append(Spacer(1, 8))

content.append(PageBreak())

# Answer Key
content.append(Paragraph("✅ Answer Key", styles["SummaryHeader"]))

answer_data = [["Q.No", "Answer"]] + [[str(i), ans] for i, (_, _, ans) in enumerate(questions, 1)]
answer_table = Table(answer_data, colWidths=[50, 80])
answer_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
]))
content.append(answer_table)

# Build PDF
doc.build(content)

print(f"✅ PDF generated successfully: {quiz_pdf}")
