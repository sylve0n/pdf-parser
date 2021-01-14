import fitz
import os
from pathlib import Path

directory_in_str = "pdfs"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    pdfBt = os.fsencode(file)
    pdf_document = "pdfs/" + pdfBt.decode("utf-8")
    
    if Path(pdf_document).suffix == ".pdf":
        doc = fitz.open(pdf_document)
        print(pdf_document)

    for current_page in range(len(doc)):
        page = doc.loadPage(current_page)
        pageText = page.getText("text")
        # print(current_page)
        file = open("pdf-txt.txt", "a+", encoding="utf8")
        file.write(pageText)
        file.close()

#TODO:
# Remove unwanted characters, IE ‖ (U+2016), ‗ (U+2017), ― (U+2015), „ (U+201E)