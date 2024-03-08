import PyPDF2

def read_pdffile(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        content = ""
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            content+= page.extract_text()
        return content
