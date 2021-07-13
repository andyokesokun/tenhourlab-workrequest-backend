from datetime import datetime
from functools import partial
from application.utils import formatDurationTime
from ..models import Service,Employee, WorkOrder
from .. import db
from ..schemas import ServiceSchema, WorkOrderSchema
from sqlalchemy import  func
from dateutil.parser import *

class WorkService():
  
    @staticmethod
    def getAllServices():
        services=Service.query.all()
        data=ServiceSchema(many=True, only=("id","name", "duration")).dump(services)
        print(services[0].name)
        for d in data:
            d["duration"] = formatDurationTime(d["duration"])

        return data;

    @staticmethod
    def createWorkOrder(customerId,serviceId, orderDate):
        orderDate = parse(orderDate)
        employee =  WorkService.assignWorkLoadToAvailableEmployee(orderDate)
        workOrder=WorkOrder(customerId,serviceId, employee.id,orderDate ) 
        db.session.add(workOrder)
        db.session.commit()
        return WorkOrderSchema().dump(workOrder)


    @staticmethod
    def  assignWorkLoadToAvailableEmployee(orderDate):
        return Employee.query.order_by(func.rand()).limit(1).first()  

    @staticmethod
    def getWorkServices():
        works = WorkOrder.query.all()
        data = WorkOrderSchema(many =True).dump(works)

        return data



      