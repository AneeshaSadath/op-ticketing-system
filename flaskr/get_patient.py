import json
import logging
from flask import request, jsonify, current_app, Blueprint
from mongoengine import OperationError, DoesNotExist
from flaskr.models import PatientData
from tasks import op_ticket_generator

get_patient_api = Blueprint("get_patient_api", __name__)


@get_patient_api.route("/get_patient", methods=["GET"])
def get_patient_by_id():
    patient_id = request.args.get("Id")
    if not patient_id:
        return jsonify({"error": "request body not found"}), 400
    try:
        details = json.loads(
            PatientData.objects.get(id=patient_id).to_json(indent=2)
        )
        op_ticket_generator.delay(str(patient_id), details)
        current_app.logger.info(
            f"Getting details:{details['first_name']+' '+details['last_name']}"
        )
        return jsonify({"response": "Got patient details successfully"})
    except (OperationError, DoesNotExist) as e:
        logging.exception(f"Error in getting patient details , error={e}")
        return jsonify({"message": "Unexpected error"}), 500
