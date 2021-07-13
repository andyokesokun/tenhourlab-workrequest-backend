from flask import app
from application import createApp
import unittest
import pytest


def test_create_work_service_should_200(client,testdata):    
      
        response=client.post("/api/v1/services/create-work-load",json =testdata)

        assert response.status_code  == 201 

def test_create_work_service_with_unvailable_service_id_should_404(client,testdata): 
        testdata["serviceId"] = 8

        response=client.post("/api/v1/services/create-work-load",json = testdata)

        assert response.status_code  == 400 

def test_create_work_service_with_not_valid_email_id_should_404(client, testdata): 
        
        testdata["customerId"] = "aokesokun" 
        response=client.post("/api/v1/services/create-work-load",json = testdata)

        assert response.status_code  == 400 

def test_create_work_service_with_missing_payload_should_404(client, testdata):  
        del testdata["customerId"]  
        print(testdata)
        response=client.post("/api/v1/services/create-work-load",json = testdata)

        assert response.status_code  == 400 

if __name__  == '__main__':
    unittest.main()
    

