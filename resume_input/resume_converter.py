import os
import pdfplumber
import docx

def convert_to_text(file_path: str) -> str:
    """
    convert a resume file (.pdf or .docx) to plain text.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("The specified file does not exist.")

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return _extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return  _extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Use .pdf or .docx only.")

def _extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def _extract_text_from_docx(file_path:str)->str:
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])
