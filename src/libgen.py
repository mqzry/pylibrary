import requests
# TODO: choose important fields, so we the json objects are a fraction of the size


libgen_api_url = "http://gen.lib.rus.ec/json.php"


def get(ids):
    payload = {'ids': ','.join(ids),
               'fields': '*'}
    response = requests.get(libgen_api_url, params=payload)
    print(response)
    if response:
        response_json = response.json()
        ret_dict = {entry['id']: entry for entry in response_json}
        return ret_dict

# def download(id):
