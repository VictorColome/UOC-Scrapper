import json
import ntpath

import requests


def get_token():
    f = open("token.txt", "r")
    return f.read()


def upload_csv(token, csv_path_to_file):
    print("\nRequesting access to Zenodo...")
    while True:
        r = requests.get('https://zenodo.org/api/deposit/depositions', params={'access_token': token})
        if r.status_code == 200:
            break

    print("Granted!")
    print("\nPreparing upload...")
    headers = {"Content-Type": "application/json"}
    while True:
        r = requests.post('https://zenodo.org/api/deposit/depositions',
                          params={'access_token': token}, json={},
                          headers=headers)
        if r.status_code == 201:
            break
    print("Upload successfully prepared with ID={}".format(r.json()['id']))

    print("\nUploading file...")
    deposition_id = r.json()['id']
    data = {'name': ntpath.basename(csv_path_to_file)}
    files = {'file': open(csv_path_to_file, 'rb')}
    while True:
        r = requests.post('https://zenodo.org/api/deposit/depositions/%s/files' % deposition_id,
                          params={'access_token': token}, data=data,
                          files=files)
        if r.status_code == 201:
            break
    print("Upload successful")

    print("\nUpdating metadata...")
    data = {
        'metadata': {
            'title': 'Dataset de la práctica',
            'upload_type': 'poster',
            'description': 'Este fichero contiene un ejemplo real del tipo de datos que se pueden encontrar al ejecutar el scraper',
            'creators': [{'name': 'Víctor Colomé y Carlos Marcos',
                          'affiliation': 'UOC'}]
        }
    }
    while True:
        r = requests.put('https://zenodo.org/api/deposit/depositions/%s' % deposition_id,
                         params={'access_token': token}, data=json.dumps(data),
                         headers=headers)
        if r.status_code == 200:
            break
        print(r.status_code)
        print(r.text)
    print("Metadata successfully updated")

    print("\nPublishing file...")
    while True:
        r = requests.post('https://zenodo.org/api/deposit/depositions/%s/actions/publish' % deposition_id,
                          params={'access_token': token})
        if r.status_code == 202:
            break
    print(r.text)
    print("File successfully published with link {}".format(r.json()["files"][0]["links"]["download"]))


if __name__ == '__main__':
    access_token = get_token()
    upload_csv(access_token, "../sample/csv/adaptador-usb_articles_attributes_20200406.csv")
