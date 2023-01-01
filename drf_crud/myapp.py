import requests
import json

url =  "http://127.0.0.1:8000/studentapi"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {"id":1}
    json_data = json.dumps(data)
    print(json_data)
    res = requests.get(url=url, data = json_data)
    print(res.status_code)
    data = res.json()
    print(data)

# get_data(2)

def post_data():
    data = {
        'name':'Rohan',
        'roll':124,
        'city':'Bokaro'
    }
    json_data = json.dumps(data)
    res = requests.post(url=url, data = json_data)
    data = res.json()
    print(data)

post_data()


def update_data():
    data = {
        'id':5,
        'name':'rohit',
        'city':'Delhi'
    }
    json_data = json.dumps(data)
    res = requests.put(url=url, data = json_data)
    data = res.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id':4
    }
    json_data = json.dumps(data)
    res = requests.delete(url=url, data = json_data)
    data = res.json()
    print(data)

# delete_data()