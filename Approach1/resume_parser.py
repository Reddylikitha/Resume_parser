from fileReaderPdf import read_pdffile
from fileReaderDocx import read_docxfile
from openai_embedding import get_embeddings, save_embeddings
from textProcess import process_text

def get_file_path():
    return file_path

file_path = input("Enter the file path")
file_path = file_path.strip('"')
if(file_path.endswith("pdf")):
    file_contents = read_pdffile(file_path)
    # print(json.loads(ask_openai(file_contents)))
    processed_file_contents = process_text(file_contents)
    embeddings = get_embeddings(processed_file_contents)
    save_embeddings(embeddings,file_path)
    
elif(file_path.endswith("docx")):
    file_contents = read_docxfile(file_path)
    processed_file_contents = process_text(file_contents)
    embeddings = get_embeddings(processed_file_contents)
    save_embeddings(embeddings,file_path)
    # print(json.loads(ask_openai(file_contents)))
else:
    print("Only pdf and docx file formats are allowed")