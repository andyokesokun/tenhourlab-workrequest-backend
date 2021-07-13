from application import createApp
from flask import request
import pytest

@pytest.fixture(scope='module')
def client():
    app =createApp()                   
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='module')       
def  testdata():
     return  {"customerId":"aokesokun@gmail.com", 
              "serviceId": "1",
              "orderDate":"2021-07-11T21:13:22.614Z"}
