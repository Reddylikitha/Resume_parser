from docx2python import docx2python

def read_docxfile(file_path):
    content = ""
    with docx2python(file_path) as docx_content:
        content += docx_content.text
    docx_content.close()
    return content
