from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors

# Create enhanced PDF file
quiz_pdf_enhanced = "JS_Quiz_25Q_Enhanced.pdf"
doc = SimpleDocTemplate(quiz_pdf_enhanced, pagesize=A4)

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CenterTitle", fontSize=18, alignment=TA_CENTER, spaceAfter=20, textColor=colors.darkblue, leading=22))
styles.add(ParagraphStyle(name="Question", fontSize=11, alignment=TA_LEFT, spaceAfter=6, leading=14, textColor=colors.black))
styles.add(ParagraphStyle(name="Option", fontSize=10, alignment=TA_LEFT, leftIndent=20, leading=12))
styles.add(ParagraphStyle(name="AnswerKey", fontSize=11, alignment=TA_LEFT, textColor=colors.darkgreen, spaceAfter=6))

# Content list
content = []

# Title Page
content.append(Paragraph("📘 JavaScript Basics Quiz – 25 Questions", styles["CenterTitle"]))
content.append(Spacer(1, 20))
content.append(Paragraph("This quiz covers **Programming Language basics, JavaScript introduction, variables, and data types**.<br/>"
                         "Each question has four options (A–D).<br/>"
                         "👉 The **Answer Key** is provided at the end.", styles["Question"]))
content.append(PageBreak())

# Questions with options (same data as before)
questions = [
    ("What is a programming language?", ["A way to talk to humans", "A way to give instructions to a computer", "A type of operating system", "A design tool"], "B"),
    ("Why can't we communicate with a computer in plain English?", ["Computers only understand 0s and 1s", "Computers are lazy", "Computers only know math", "Because English is too complex"], "A"),
    ("Which analogy best describes a programming language?", ["Like a recipe book", "Like a movie script", "Like a painting", "Like a hammer"], "B"),
    ("What is JavaScript mainly used for?", ["Designing databases", "Making websites interactive", "Compiling code", "Editing images"], "B"),
    ("Where can JavaScript run?", ["Browser, Server, Mobile apps", "Only in browsers", "Only in Windows OS", "Only in Android"], "A"),
    ("In the restaurant analogy, JavaScript is like:", ["Walls", "Lights", "Waiter", "Menu"], "C"),
    ("What is a variable?", ["A fixed constant", "A container for data", "A function", "A server"], "B"),
    ("Analogy for a variable is:", ["A chair", "A jar with label", "A switch", "A bank account"], "B"),
    ("Which is correct variable declaration in JS?", ["var age = 25;", "let age = 25;", "const age = 25;", "All of the above"], "D"),
    ("Which keyword creates a constant variable?", ["let", "const", "var", "static"], "B"),
    ("JavaScript data types fall into how many main categories?", ["1", "2", "3", "4"], "B"),
    ("How many primitive data types exist in JS?", ["5", "6", "7", "8"], "C"),
    ("Difference between null and undefined?", ["Same thing", "undefined = not assigned, null = empty", "null = error, undefined = correct", "null is older"], "B"),
    ("Analogy for undefined is:", ["Reserved empty table", "Empty jar with label", "A switch", "Unique ID card"], "B"),
    ("Analogy for null is:", ["Reserved empty table", "Jar with label", "Light bulb", "Menu"], "A"),
    ("Symbol in JS represents:", ["A picture", "A unique identifier", "An emoji", "A Boolean"], "B"),
    ("BigInt is used for:", ["Small numbers", "Huge integers beyond Number limit", "Decimal values", "Symbols"], "B"),
    ("Arrays are:", ["Key-value pairs", "Ordered lists", "Functions", "Data types"], "B"),
    ("Objects are:", ["Unordered key-value pairs", "Lists", "Numbers", "Functions only"], "A"),
    ("Output of `let x; console.log(x);`?", ["null", "undefined", "error", "0"], "B"),
    ("typeof null gives:", ["object", "null", "undefined", "error"], "A"),
    ("typeof true gives:", ["boolean", "string", "number", "true"], "A"),
    ("Output: `console.log(`Hi, I'm Alice, 25 years old.`)`?", ["Alice 25", "Error", "Hi, I'm Alice, 25 years old.", "undefined"], "C"),
    ("Boolean analogy:", ["Jar", "Switch", "VIP Pass", "Recipe"], "B"),
    ("Function analogy:", ["Coffee machine", "Table", "Switch", "Jar"], "A"),
    ("Why are analogies important?", ["They confuse learners", "They simplify concepts", "They are decorative", "They are jokes"], "B")
]

# Add questions with visual styling (table boxes)
for i, (q, opts, ans) in enumerate(questions, 1):
    q_table = Table([[f"Q{i}. {q}"]], colWidths=[500])
    q_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.lightblue),
                                 ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                                 ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
                                 ("FONTSIZE", (0, 0), (-1, -1), 10),
                                 ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                                 ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                 ("BOX", (0, 0), (-1, -1), 1, colors.darkblue),
                                 ("PADDING", (0, 0), (-1, -1), 6)]))
    content.append(q_table)
    for j, opt in zip(["A", "B", "C", "D"], opts):
        content.append(Paragraph(f"{j}. {opt}", styles["Option"]))
    content.append(Spacer(1, 8))

content.append(PageBreak())

# Answer Key with colored table
content.append(Paragraph("✅ Answer Key", styles["CenterTitle"]))

answer_data = [["Q.No", "Answer"]] + [[str(i), ans] for i, (_, _, ans) in enumerate(questions, 1)]
answer_table = Table(answer_data, colWidths=[50, 80])
answer_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                                  ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                                  ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                                  ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                                  ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                                  ("FONTSIZE", (0, 0), (-1, -1), 10),
                                  ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke)]))
content.append(answer_table)

# Build PDF
doc.build(content)

quiz_pdf_enhanced
