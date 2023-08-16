import fitz  # PyMuPDF

def extract_sections(pdf_path, section_keywords):
    doc = fitz.open(pdf_path)
    sections = {}
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = page.get_text()
        
        for section_name in section_keywords:
            if section_name.lower() in text.lower():
                start_idx = text.lower().index(section_name.lower())
                end_idx = start_idx + len(section_name)
                section_text = text[end_idx:]
                
                # Find the next section's start index if it exists
                next_section_start_idx = len(section_text)
                for next_section in section_keywords:
                    next_section_idx = section_text.lower().find(next_section.lower())
                    if next_section_idx != -1 and next_section_idx < next_section_start_idx:
                        next_section_start_idx = next_section_idx
                
                section_text = section_text[:next_section_start_idx].strip()
                
                if section_name in sections:
                    sections[section_name].append(section_text)
                else:
                    sections[section_name] = [section_text]
    
    doc.close()
    return sections

if __name__ == "__main__":
    pdf_path = "your_pdf_file.pdf"
    section_keywords = ["section 1", "section 2", "section 3"]  # Add your section keywords here
    
    extracted_sections = extract_sections(pdf_path, section_keywords)
    
    for section_name, section_texts in extracted_sections.items():
        print(f"{section_name}:")
        for i, section_text in enumerate(section_texts, start=1):
            print(f"Subsection {i}: {section_text}\n")
