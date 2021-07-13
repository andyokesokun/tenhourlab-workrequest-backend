from flask.json import dump
from flask_sqlalchemy import model
from sqlalchemy.orm import load_only
from sqlalchemy.sql.expression import null
from application import models
from . import db 
from . import ma 
from marshmallow import ValidationError,fields,validates,Schema 

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        model = models.Employee
     

class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        model = models.Service
       

class WorkOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        include_fk =True
        model =models.WorkOrder
       
     

    customerId =fields.Email(required = True) 
    serviceId =ma.auto_field(load_only = True)
    employeeId =ma.auto_field(dump_only= True,load_only=True ) 
    service = fields.Nested(ServiceSchema())
    employee = fields.Nested(EmployeeSchema())


    @validates("serviceId")
    def  validateServiceId(self,serviceId) :
        print("serviceId %s" %serviceId)
        service=models.Service.query.get(serviceId)
        print( "service %s" %service)
        if service == None :
            raise  ValidationError("Invalid service Id")


            





