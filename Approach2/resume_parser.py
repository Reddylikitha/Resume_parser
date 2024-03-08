from Approach2.fileReaderDocx import read_docxfile
from fileReaderPdf import read_pdffile
from approach2 import ask_openai
from openai_embeddings import get_embeddings, save_embeddings

file_path = input("Enter the file path")
file_path = file_path.strip('"')
file_contents=""
if(file_path.endswith("pdf")):
    file_contents = read_pdffile(file_path)
    resume_json=ask_openai(file_contents)
    embeddings = get_embeddings(resume_json)
    save_embeddings(embeddings,file_path)
elif(file_path.endswith("docx")):
    file_contents = read_docxfile(file_path)
    resume_json=ask_openai(file_contents)
    embeddings = get_embeddings(resume_json)
    save_embeddings(embeddings,file_path)
    
else:
    print("Only pdf and docx file formats are supported.....!")