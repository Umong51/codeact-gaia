from pypdf import PdfReader
from smolagents import tool


@tool
def read_pdf_file(file_path: str) -> str:
    """
    This function reads the first three pages of a PDF file and returns its content as a string.
    Args:
        file_path: The path to the PDF file.
    Returns:
        A string containing the content of the PDF file.
    """
    content = ""
    reader = PdfReader(file_path)
    print(len(reader.pages))
    pages = reader.pages[:3]
    for page in pages:
        content += page.extract_text()
    return content
