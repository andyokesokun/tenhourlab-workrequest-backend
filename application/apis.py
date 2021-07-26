from marshmallow.fields import Method
from werkzeug import utils
from application.schemas import ServiceTimeSlotSchema, WorkOrderSchema
from flask import current_app as app, jsonify, request
from application.services.WorkService import WorkService
from marshmallow import ValidationError




@app.route("/")
def index():
    return "Welcome Andrew" 

@app.route("/api/v1/services")
def  getServices(): 
    return  jsonify(WorkService.getAllServices())

@app.route("/api/v1/services/create-work-load", methods=["POST"])
def createWorkLoad():
     data=request.get_json()
     try:
        #valiate payload
        WorkOrderSchema().load(data)
        workOrder=WorkService.createWorkOrder(data["customerId"],data["serviceId"], data["startDate"])
        return jsonify(workOrder),201
        
     except ValidationError as err:
         print(err)
         return jsonify(err.messages),400

@app.route("/api/v1/services/work-services")
def getWorkServices():
    return jsonify(WorkService.getWorkServices())

@app.route("/api/v1/services/check-available-time-slot", methods =["POST"])
def checkAvailableTimeSlot():
    data =request.get_json()
    try:
        ServiceTimeSlotSchema.load(data)   
        availabe=WorkService.checkIfBookDateAvailable(data["serviceId"], data["startDate"])
        if availabe :
            return jsonify({"status":"available"}),200
        else:
            return jsonify({"status":"unavailable"}),200


    except ValidationError as err:
        print(err)
        return jsonify(err.messages),400
    



    
