# auth info for DB
import auth
import requests
from base64 import b64encode, b64decode

library_db = "https://yyhye.cloudant.com/library"


def add_attachment(doc, attachment, name, content_type):
    if attachment is not None:
        with open(attachment, 'rb') as f:
            doc['_attachments'] = {}
            doc['_attachments'][name] = {
                'content_type': content_type,
                'data': b64encode(f.read()).decode('utf-8')
            }
    return doc


def get_all_documents():
    return query('_all_docs')


def query(method, params):
    result = requests.get(library_db + "/" + method, params=params,
                          auth=(auth.user, auth.password))
    return result.json()


def create(doc):
    result = requests.post(library_db, json=doc, auth=(auth.user, auth.password))
    print(result)
    return result.json()
