# auth info for DB
import auth
import requests
import mimetypes
import os
from base64 import b64encode


class CouchDB:

    def __init__(self, url, auth):
        self.base_url = url
        self.auth = auth

    def set_current_db(self, db):
        self.db = db
        self.db_url = self.base_url + db

    def create(self, doc):
        result = requests.post(self.db_url, json=doc,
                               auth=(self.auth.user, self.auth.password))
        return result.json()

    def update(self, doc):
        result = requests.post(self.db_url + doc['_id'], json=doc,
                               auth=(auth.user, auth.password))
        return result.json()

    def get(self, id):
        result = requests.get(self.db_url + id,
                              auth=(auth.user, auth.password))
        return result.json()

    def query(self, method, params=None):
        response = requests.get(self.db_url + method, params=params,
                                auth=(auth.user, auth.password))
        return response.json()

    def put_bulk(self, docs):
        return self.query(self, '_bulk_docs', {'docs': docs})

    def get_bulk(self, ids):
        payload = {'keys': ids}
        return self.query(self, '_all_docs', payload)

    def get_all(self):
        return self.query(self, '_all_docs')

    def add_attachment(doc, attachment_path, name=None, content_type=None):
        if attachment_path:
            if not name:
                name = os.path.basename(attachment_path)
            if not content_type:
                content_type = mimetypes.guess_type(attachment_path)[0]
            with open(attachment_path, 'rb') as f:
                doc['_attachments'] = {}
                doc['_attachments'][name] = {
                    'content_type': content_type,
                    'data': b64encode(f.read()).decode('utf-8')
                }
        return doc

    def replicate(self, source, target):
        doc = {'source': self.base_url + source, 'target': self.base_url + target, "create_target": True}
        self.set_current_db('_replicator')
        return self.create(doc)

    def create_db(self, name):
        return requests.put(self.base_url + name)

    def delete_db(self, name):
        return requests.delete(self.base_url + name)

    def get_view(self, design_doc, view_name):
        response = requests.get(self.db_url + "_design/{0}/_view/{1}".format(design_doc, view_name))
        return response


class Cloudant(CouchDB):

    def __init__(self, user, password):
        self.base_url = 'https://{}.cloudant.com/'.format(user)
        self.auth = {'user': user, 'password': password}
