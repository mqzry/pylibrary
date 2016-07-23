# !/usr/bin/env python

import glob
import db


fileformats = ['pdf', 'epub', 'djvu']
root_library = "C:\\Users\\Sadari\\Documents\\Library"


def get_all_docs(dir):
    all_docs = []
    for key in fileformats:
        path = (dir + '\**\*.{}').format(key)
        all_docs.extend(glob.glob(path, recursive=True))

    return all_docs


def cl_submit_metadata(dir):
    all_docs = get_all_docs(dir)

    print("""Write medata line by line as key value pairs.
Write lists comma separated.
A blank line indicates the end of the metadata.\n""")

    for file_path in all_docs:
        metadata = collect_metadata(file_path)
        db.put_doc(file_path, metadata)


def collect_metadata(item_name):
    # Announce that user should supply metadata for current item
    print(item_name)

    metadata = {}
    while True:
        input_str = input("")
        if input_str == '':
            break
        elif input_str == 'skip':
            break

        split_input = input_str.split(':')
        key = split_input[0].strip()
        value = split_input[1].split(', ')
        if len(value) > 1:
            metadata[key] = [x.strip() for x in value]
        else:
            metadata[key] = value[0]

    return metadata
