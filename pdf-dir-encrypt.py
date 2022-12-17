# pdf paranoia
import PyPDF2
import os
from pathlib import Path
import glob
import shutil
import sys

# enter password to encrypt all pdfs with
if len(sys.argv) < 2:
    print("Usage: python3 pdf-paranoia.py [password_to_encrypt]" )
    sys.exit()
elif len(sys.argv) == 2:
    password = sys.argv[1]
    pdfFiles = []
    for filename in os.listdir('pdf-files'):
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)
            filepath = os.path.join('pdf-files', filename)
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
    