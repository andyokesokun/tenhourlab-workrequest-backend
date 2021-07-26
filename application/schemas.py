from datetime import datetime

from marshmallow.decorators import validates_schema
from application.utils import format_duration_time, get_end_date, to_date_string
from flask.json import dump
from flask_sqlalchemy import model
from sqlalchemy.orm import load_only
from sqlalchemy.sql.expression import null, true
from application import models
from application.services.WorkService import WorkService
from . import db 
from . import ma 
from marshmallow import ValidationError,fields,validates,Schema 



def  validate_service_id(serviceId) :
    service=models.Service.query.get(serviceId)
    if service == None :
        raise  ValidationError("Invalid service Id")


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        model = models.Employee
    
    createdAt =ma.auto_field(load_only= True )
    updatedAt =ma.auto_field(load_only=True )
     

class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        model = models.Service

    createdAt =ma.auto_field(load_only= True )
    updatedAt =ma.auto_field(load_only=True )
    duration =fields.Method("get_service_time")

    def get_service_time(self, obj):
        return format_duration_time(obj.duration)
   


class WorkOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        include_fk =True
        model =models.WorkOrder
       
    title = fields.Method("get_title")
    createdAt =ma.auto_field(load_only= True )
    customerId =fields.Email(required = True, load_only=True) 
    serviceId =ma.auto_field(load_only = True, validates=validate_service_id)
    employeeId =ma.auto_field(dump_only= True,load_only=True ) 
    # service = fields.Nested(ServiceSchema())
    # employee =fields.Nested(EmployeeSchema())
    endDate = fields.Method("get_end_date")


    def get_end_date(self, obj ):
        
           date=get_end_date(obj.startDate, format_duration_time(obj.service.duration))
           return to_date_string(date)
        
    
    def get_title(self, obj):
        return obj.service.name
    

    # @validates("serviceId")
    # def  validate_service_id(self,serviceId) :
    #     service=models.Service.query.get(serviceId)
    #     if service == None :
    #         raise  ValidationError("Invalid service Id")
    
    
    @validates_schema
    def  validate_start_date(self,data,**kwargs) :
        today = datetime.now()
        startDate = data["startDate"]
    
        if startDate < today :
            raise  ValidationError("Can't book in the past")
    
        serviceId =data["serviceId"]
        available=WorkService.checkIfBookDateAvailable(serviceId,  to_date_string(startDate))  
        if not available :
             raise  ValidationError("Time Slot not available")



class ServiceTimeSlotSchema(ma.Schema):
    serviceId = ma.Integer(required = True, validates=validate_service_id)
    startDate = ma.DateTime(required = True)








