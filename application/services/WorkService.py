from datetime import datetime
from operator import and_

from sqlalchemy.sql.expression import false, true
from application.utils import format_duration_time, get_end_date, to_date_string
from ..models import Service,Employee, WorkOrder
from .. import db
import application.schemas as schemas
from sqlalchemy import  func
from dateutil.parser import *

class WorkService():
  
    @staticmethod
    def getAllServices():
        services=Service.query.all()
        return schemas.ServiceSchema(many=True).dump(services)
    
    
    @staticmethod
    def getServiceById(serviceId):
        service =Service.query.get(serviceId)
        return schemas.ServiceSchema().dump(service)

        

    @staticmethod
    def createWorkOrder(customerId,serviceId, startDate):
        startDate = parse(startDate)
        employee =  WorkService.assignWorkLoadToAvailableEmployee(startDate)
        workOrder=WorkOrder(customerId,serviceId, employee.id,startDate ) 
        db.session.add(workOrder)
        db.session.commit()
        return schemas.WorkOrderSchema().dump(workOrder)
        

    @staticmethod
    def  assignWorkLoadToAvailableEmployee(startDate):
        return Employee.query.order_by(func.rand()).limit(1).first()  

    @staticmethod
    def getWorkServices():
        works = WorkOrder.query.all()
        return  schemas.WorkOrderSchema(many =True).dump(works)

    @staticmethod
    def checkIfBookDateAvailable(serviceId, startDateStr):
        today = datetime.now()
        works =WorkOrder.query.filter_by(serviceId = serviceId).filter(WorkOrder.startDate >= today).all()

        data=schemas.WorkOrderSchema(many =True).dump(works)

        for workOrder in data:
             # booking done within and allocated time 
             if startDateStr >= workOrder["startDate"] and startDateStr <= workOrder["endDate"]:  
                 return  False
        
        return True
       

        



      