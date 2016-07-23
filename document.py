import os
import mimetypes
import requests

class Document:

    def __init__(self, metadata, file_path=None, url=None):
        self.metadata = metadata
        self.file_path = file_path
        self.url = url

    def create_offline_doc(self):
        doc = self.metadata
        ext = os.path.basename(self.file_path).split('.')[1]
        return add_attachment(doc, self.file_path, ext)

    def create_online_doc(self, metadata, url):
        doc = requests.get(url).content
        return self.create_doc(doc, metadata)
