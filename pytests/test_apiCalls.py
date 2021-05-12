from time import sleep
import names
from RandomWordGenerator import RandomWord
import requests
import json
import random
import pytest


rw = RandomWord()
#Datos API
base='http://localhost:5000/'
datype={'Content-type':'application/json'}

randomData = []
for i in range (0,10):
    randomData.append(
        (names.get_first_name(), 1000*random.randrange(1,10), rw.generate())
    )


@pytest.mark.parametrize("userid, name", [(1,"Luke"),(3,"David")])
def test_employee_by_id(supply_url,userid,name):
    response = requests.get(supply_url+'employees/'+str(userid))
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['id'] == userid
    assert response_data['name'] == name

def test_nf_employee_by_id(supply_url, id = 0):
    response = requests.get(supply_url+'employees/'+str(id))
    assert response.status_code == 500



def test_create_employee(supply_url): 
    dummyData = { 'name': 'PepitoTest', 'salary': 1000, 'position': 'test'}
    response = requests.post(supply_url+'employees',data = json.dumps(dummyData), headers={'Content-type':'application/json'})
    response_data = response.json()
    assert response.status_code == 201
    assert response_data['name'] == 'PepitoTest'
    assert requests.delete(supply_url+'employees/'+ str(response_data['id'])).ok

def test_patch_employee(supply_url):
    dummyPatch = { "name": "PepitoTestChanged"}
    backToOriginal = { "name": "Luke"}
    response = requests.patch(supply_url+'employees/1',data = json.dumps(dummyPatch), headers={'Content-type':'application/json'})
    response_data = response.json()
    assert response.status_code == 201
    assert response_data['name'] == 'PepitoTestChanged'
    response2 = requests.patch(supply_url+'employees/1',data = json.dumps(backToOriginal), headers={'Content-type':'application/json'})
    assert response2.status_code == 201
    assert response2.json()['name'] == 'Luke'

@pytest.mark.parametrize("name, salary, position",randomData)
def test_CRUD_emplyoee(supply_url,name, salary, position):
    dummyData = { 'name': name, 'salary': salary, 'position': position}
    dummyPatch = { "name": name+"-changed"}
    #POST
    response_post = requests.post(supply_url+'employees',data = json.dumps(dummyData), headers={'Content-type':'application/json'})
    response_data_post = response_post.json()
    employeeid = response_data_post['id']
    employeeName = response_data_post['name'] 
    assert response_post.status_code == 201
    assert employeeName == name
    #GET BY ID
    test_employee_by_id(supply_url,employeeid,employeeName)
    #PATCH
    response_patch = requests.patch(supply_url+'employees/'+str(employeeid),data = json.dumps(dummyPatch), headers={'Content-type':'application/json'})
    assert response_patch.json()['name'] == employeeName+'-changed'
    #DELETE
    assert requests.delete(supply_url+'employees/'+ str(employeeid)).ok
    #GET NOT FOUND
    test_nf_employee_by_id(supply_url,employeeid)
    sleep(0.5)
    
