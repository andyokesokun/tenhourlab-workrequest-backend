from datetime import datetime

from sqlalchemy.orm import backref
from . import db

class Service(db.Model):
    __tablename__ ="services"
    id=db.Column(db.Integer,primary_key = True)
    name= db.Column(db.Text,nullable=False)
    duration = db.Column(db.String(20))
    createdAt = db.Column(db.DateTime,nullable=False, default = datetime.now)
    updatedAt = db.Column(db.DateTime,nullable=False, default = datetime.now)

    workOrders = db.relationship("WorkOrder", backref =backref("service",lazy='joined'))
    

    def __init__(self,name, duration):
        self.name = name
        self.duration =duration
    


class Employee(db.Model):
    __tablename__ ="employees"
    id=db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    createdAt = db.Column(db.DateTime,nullable=False, default = datetime.now)
    updatedAt = db.Column(db.DateTime,nullable=False, default = datetime.now)
    WorkOrders =db.relationship("WorkOrder", backref =backref("employee",lazy="joined"))


    def __init__(self,name):
       self.name = name


class WorkOrder(db.Model):
    __tablename__ ="workOrders"
    id=db.Column(db.Integer,primary_key = True)
    customerId= db.Column(db.String(100),nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False, default = datetime.now)
    startDate = db.Column(db.DateTime,nullable=False, index=True)

    serviceId = db.Column(db.Integer, db.ForeignKey("services.id"), nullable = False)
    employeeId = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable = False)
    

    def __init__(self,customerId,serviceId,employeeId,startDate):
       self.serviceId = serviceId
       self.customerId = customerId
       self.employeeId =employeeId
       self.startDate = startDate





    

