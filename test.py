import fitz  # PyMuPDF
import re

def extract_headers_and_paragraphs(pdf_path):
    pdf_document = fitz.open(pdf_path)
    headers_and_paragraphs = []
    
    current_header = None
    current_paragraph = ""
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text = page.get_text("text")
        
        font_properties = []
        for block in page.get_text("blocks"):
            for line in block[4]:
                font_properties.append(line[3])  # Font properties for each line
        
        for line, font_property in zip(text.split('\n'), font_properties):
            if re.search(r'\bHeader \d+\b', line):  # Check for header format like "Header 1", "Header 2", etc.
                if current_header is not None:
                    headers_and_paragraphs.append((current_header, current_paragraph))
                current_header = line.strip()
                current_paragraph = ""
            else:
                current_paragraph += line + '\n'
    
    if current_header is not None:
        headers_and_paragraphs.append((current_header, current_paragraph))
    
    pdf_document.close()
    return headers_and_paragraphs

if __name__ == "__main__":
    pdf_path = "your_pdf_file.pdf"
    extracted_data = extract_headers_and_paragraphs(pdf_path)
    
    for header, paragraph in extracted_data:
        print(f"Header: {header}\nParagraph:\n{paragraph}")
