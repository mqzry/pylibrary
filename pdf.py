# !/usr/bin/env python

# Script to tidy your library
# 1. Sniff metadata of different fileformat(PDF, epub prio)
# 1. Format files in specified format
# 2. Build index in DB and/or JSON file
# 3. Download favourite fileformat
import requests
import base64
import glob
import os
# auth info for DB
import auth

library_db = "https://yyhye.cloudant.com/library"


def read_docs_from_bookzz(dir):
    all_docs = glob.glob(dir + '/(*.pdf|*.epub)')
    for item in all_docs:
        if str.endswith('(BookZZ.org)'):
            splitted_filename = str.split(']')
            creators = splitted_filename[0][1:]
            title = splitted_filename[1].split('(BookZZ')[0]
            doc = create_doc(creators, title, item)
            create(doc)


def add_attachment(doc, attachment, name, content_type):
    if attachment is not None:
        with open(attachment) as f:
            doc['_attachments']['name'] = {
                'content_type': content_type,
                'data': base64.b64encode(f.read())
            }
    return doc


def create_doc(creators, title, file):
    doc = {}
    doc['creators'] = creators
    doc['title'] = title
    ext = os.path.splitext(file)[1]
    if ext == 'pdf':
        add_attachment(doc, file, "pdf", "application/pdf")
    if ext == 'epub':
        add_attachment(doc, file, "epub", "application/epub+zip")
    else:
        return None

    return doc


def get_all_documents():
    return query('_all_docs')


def query(method, params):
    result = requests.get(library_db + "/" + method, params=params,
                          auth=(auth.user, auth.password))
    return result.json()


def create(doc):
    result = requests.put(library_db, doc, auth=(auth.user, auth.password))
    return result.json()


# def download_all_documents(dir):
#     result = requests.get(library_db + "/_all_docs",
#                           params={'include_docs': "true"})
#     result.json()
#     docs = result['rows']

    # for doc in docs:
    #     os.makedirs(, exist_ok = True)
    #     with open()
    #     for attachment in doc['attachments']:
    #         file = base64.b64decode(attachment['data'])
