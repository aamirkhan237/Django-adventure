import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data={}
    if id is not None:
        data={"id":id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data) # it will through response which we will be store in r
    data=r.json()
    print(data)

# get_data()


def post_data():
    data={
        'name':"Ravi",
        'roll':44,
        'city':'rancHi',
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

# post_data()


def update_data():
    data={
        'id':7,
        'name':"messi",
        'city':'Bookaro',
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

# update_data()

def delete_data():
    data={
        'id':10
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

delete_data()