from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        # Name
        self.set_font("Helvetica", 'B', 20)
        self.set_text_color(40, 40, 120)
        self.cell(0, 12, "Palak Thakur", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        
        # Contact info
        self.set_font("Helvetica", '', 11)
        self.set_text_color(0, 0, 0)
        self.cell(
            0, 6,
            "Kullu, Himachal Pradesh, India | plkthkr26@gmail.com | +91 90153 30962",
            new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C'
        )
        self.ln(4)
        
        # Line under header
        self.set_draw_color(40, 40, 120)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)

    def section_title(self, title):
        # Background rectangle for title
        self.set_fill_color(230, 230, 250)  # light lavender
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.5)
        self.set_font("Helvetica", 'B', 13)
        self.set_text_color(40, 40, 120)
        self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        
        # Underline line
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def add_list(self, items):
        for item in items:
            self.cell(0, 7, f"- {item}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

# Create PDF
pdf = PDF(format='A4')
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Helvetica", '', 12)

# Career Objective
pdf.section_title("Career Objective")
pdf.multi_cell(
    0, 7,
    "Motivated and detail-oriented Bachelor of Computer Applications (BCA) graduate (2025), eager to start a career in the IT industry. Strong foundation in computer science concepts, problem-solving, and web technologies. Looking for an opportunity to apply academic knowledge to real-world projects and grow as a professional."
)
pdf.ln(3)

# Education
pdf.section_title("Education")
pdf.multi_cell(
    0, 7,
    "- Bachelor of Computer Applications (BCA) - Completed 2025\n"
    "  Rajyog Kanya Mahavidyalay, Lakkar Bazar, Shimla (HP)\n"
    "  Himachal Pradesh University\n\n"
    "- Senior Secondary (12th, Arts) - 2022\n"
    "  Government Girls Senior Secondary School, Anni\n"
    "  Himachal Pradesh Board of School Education\n\n"
    "- Secondary (10th) - 2020\n"
    "  Government Girls Senior Secondary School, Anni\n"
    "  Himachal Pradesh Board of School Education"
)
pdf.ln(2)

# Soft Skills
pdf.section_title("Soft Skills")
soft_skills = ["Communication Skills", "Teamwork & Collaboration", "Problem-Solving", "Adaptability & Quick Learner", "Time Management"]
pdf.add_list(soft_skills)

# Achievements
pdf.section_title("Achievements")
achievements = ["Active participant in college technical events."]
pdf.add_list(achievements)

# Interests
pdf.section_title("Interests")
interests = ["Travelling", "Painting"]
pdf.add_list(interests)

# Save PDF
pdf_file_path = r"D:\My work\Python\03\Palak_Thakur_Resume_Styled_Professional.pdf"
pdf.output(pdf_file_path)
print("PDF successfully created at:", pdf_file_path)
