from marshmallow.fields import Method
from application.schemas import WorkOrderSchema
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
        data=WorkService.createWorkOrder(data["customerId"],data["serviceId"], data["orderDate"])
        return jsonify(data),201
     except ValidationError as err:
         print(err)
         return jsonify(err.messages),400

@app.route("/api/v1/services/work-services")
def getWorkServices():
    return jsonify(WorkService.getWorkServices())
    
