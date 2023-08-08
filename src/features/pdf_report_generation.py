```python
import os
from fpdf import FPDF
from src.shared_dependencies import report_data, ReportSchema

class PDFReportGenerator(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Social Media Management Tool Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

def generate_report():
    pdf = PDFReportGenerator()

    for chapter in report_data:
        ReportSchema().load(chapter)  # Validate data with schema
        pdf.add_chapter(chapter['title'], chapter['body'])

    pdf_file_path = os.path.join(os.getcwd(), 'reports', 'report.pdf')
    pdf.output(pdf_file_path, 'F')

    return pdf_file_path
```