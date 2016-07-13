# !/usr/bin/env python

# Script to tidy your library
# 1. Sniff metadata of different fileformat(PDF, epub prio)
# 1. Format files in specified format
# 2. Build index in DB and/or JSON file
# 3. Download favourite fileformat

from PyPDF2 import PdfFileReader
from pathlib import Path


def metadata(file):
    f = file.open('rb')
    # PdfFileReader needs a byte stream by a negative offset
    # used as argument of stream.seek(offset,..)
    pdf = PdfFileReader(f)
    metadata = {}
    metadata['internal'] = pdf.getDocumentInfo()
    metadata['xmp'] = pdf.getXmpMetadata()
    return metadata

resources_path = Path(
    ".\Resources")
pdf_files = list(resources_path.glob('**/*.pdf'))

print(pdf_files)
for file in pdf_files:
    print(metadata(file))
