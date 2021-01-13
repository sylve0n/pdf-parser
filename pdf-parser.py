import fitz
import os

directory_in_str = "pdfs"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    pdfBt = os.fsencode(file)
    pdf_document = "pdfs/" + pdfBt.decode("utf-8")
    doc = fitz.open(pdf_document)

    for current_page in range(len(doc)):
        page = doc.loadPage(current_page)
        pageText = page.getText("text")

        file = open("pdf-txt.txt", "a+", encoding="utf8")
        file.write(pageText)
        file.close()

#TODO: 
# iterate through docs to make sure they're actually pdfs
# Remove unwanted characters, IE ‖, ‗, ―