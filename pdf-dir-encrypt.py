# pdf paranoia
import PyPDF2
import os
from pathlib import Path
import glob
import shutil
import sys

# enter password to encrypt all pdfs with
if len(sys.argv) < 3:
    print("Usage: python3 pdf-paranoia.py [password_to_encrypt] [path/to/folder]" )
    sys.exit()
elif len(sys.argv) == 3:
    password = sys.argv[1]
    folder_path = sys.argv[2]
    pdfFiles = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)
            filepath = os.path.join(folder_path, filename)
    pdfFiles.sort(key = str.lower)
    pdfWriter = PyPDF2.PdfFileWriter()

   # encrypt each pdf with password in given directory in listdir
    for filename in pdfFiles:
        print(filename)
        pdfFile = open(filepath,"rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        pdfWriter.encrypt(password)
        resultPdf = open(f"encrypted_{filename}", "wb")
        pdfWriter.write(resultPdf)
        resultPdf.close()