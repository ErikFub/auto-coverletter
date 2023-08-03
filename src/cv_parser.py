"""Parsing content from CV .pdf to python string."""
import pypdfium2


def get_cv_content(file_path: str) -> str:
    pdf = pypdfium2.PdfDocument(file_path)
    text = '\n'.join([page.get_textpage().get_text_range() for page in pdf])
    return text
