import libgen
import db


def libgen(database):
    db.library_db_name = database
    libgen_entries = db.get_view('libgen')['rows']
    db_docs = db.get_bulk([entry['_id'] for entry in libgen_entries])
    libgen_docs = libgen.get([entry['value'] for entry in libgen_entries])
    new_docs = {}
    for doc in db_docs:
        doc['libgen'] = libgen_docs[doc['libgen_id']]
        new_docs.append(doc)

    db.put_bulk(new_docs)
