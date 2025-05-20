import pdfplumber

def extract_text_from_pdf(filename) -> str:
    all_text = ""
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                all_text += page_text + '\n'

    return all_text.strip()

