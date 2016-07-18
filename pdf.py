# !/usr/bin/env python

# Script to tidy your library
# 1. Sniff metadata of different fileformat(PDF, epub prio)
# 1. Format files in specified format
# 2. Build index in DB and/or JSON file
# 3. Download favourite fileformat
import glob
import os
import db

url = "http://gen.lib.rus.ec/json.php"

# def get_metadata(ids, fields="ID,Title,Author,md5"):
#     data = {}
#     data['ids'] = ids
#     data['fields'] = fields
#     response = requests.get(url, data)
#     return response.json()

def read_docs_from_bookzz(directory):
    all_docs = glob.glob(directory + '\**\*.pdf', recursive=True)
    all_docs += glob.glob(directory + '\**\*.epub', recursive=True)
    for item in all_docs:
        if item.find('(BookZZ.org)') != -1:
            splitted_filename = item.split(']')
            if len(splitted_filename) == 2:
                metadata = {}
                metadata['creators'] = splitted_filename[0].split('[')[1] \
                                                           .replace('_', ' ')
                metadata['title'] = splitted_filename[1].split('(BookZZ')[0] \
                                                        .replace('_', ' ')
                create_doc(item, metadata)


def process_all_docs(directory):
    all_docs = glob.glob(directory + '\**\*.pdf', recursive=True)
    all_docs += glob.glob(directory + '\**\*.epub', recursive=True)

    for item in all_docs:
        print(item)
        metadata = {}
        metadata['creators'] = input("What are the creators?\n")
        metadata['title'] = input("What is the title?\n")
        metadata['category'] = input("What is the category?e.g. math.topology\n")
        metadata['status'] = input("What is the status?(0=toread, 1=reading, 2=read)\n")
        metadata['md5'] = input("What is the md5 in libgen?\n")
        create_doc(item, metadata)


def create_doc(file, metadata):
    doc = metadata
    ext = os.path.splitext(file)[1]
    if ext == '.pdf':
        db.add_attachment(doc, file, "pdf", "application/pdf")
    elif ext == '.epub':
        db.add_attachment(doc, file, "epub", "application/epub+zip")
    else:
        return None
    return db.create(doc)

process_all_docs("C:\\Users\\Sadari\\Documents\\Library")
