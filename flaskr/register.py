import logging
from flask import request, jsonify, current_app, Blueprint
from mongoengine import OperationError, ValidationError
from flaskr.models import PatientData
from tasks import op_ticket_generator

register_api = Blueprint("register_api", __name__)


@register_api.route("/register", methods=["POST"])
def new_registration():
    details = request.json
    if not details:
        return jsonify({"error": "request body not found"}), 400
    try:
        patient_details = PatientData(**details).save()
        op_ticket_generator.delay(str(patient_details.id), details)
        current_app.logger.info(
            f"Saving details:{details['first_name']+' '+details['last_name']}"
        )
        return jsonify({"response": "Saved patient details successfully"})
    except (OperationError, ValidationError) as e:
        logging.exception(f"Error in saving patient details , error={e}")
        return jsonify({"message": "Unexpected error"}), 500
