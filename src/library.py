import libgen


class Library:
    def __init__:
    def get_libgen_docs:
    def update_docs:
    def create_doc:
    def download_doc:
    def download_all_docs:
    def update_libgen_docs(self):
        libgen_docs = self.get_libgen_docs()
        libgen_entries = libgen.get([doc.id for doc in libgen_docs])
        new_docs = {}
        for doc in libgen_docs:
            doc.libgen_data = libgen_entries[doc.libgen_id]
            new_docs.append(doc)

        self.update_docs(new_docs)
