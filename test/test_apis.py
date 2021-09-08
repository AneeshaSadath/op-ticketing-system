import json
from unittest import mock
import pytest
from mongoengine import ValidationError
from flaskr import app
from flaskr.models import PatientData


REGISTER_DATA = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "gender": "Female",
    "dob": "29/03/1998",
    "age": 24,
}

REGISTER_DATA_WITHOUT_FIRTS_NAME = {
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "gender": "Female",
    "dob": "29/03/1998",
    "age": 24,
}

REGISTER_DATA_WITHOUT_LAST_NAME = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "gender": "Female",
    "dob": "29/03/1998",
    "age": 24,
}

REGISTER_DATAWITHOUT_ADDRESS_1 = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "gender": "Female",
    "dob": "29/03/1998",
    "age": 24,
}

REGISTER_DATA_WITHOUT_GENDER = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "dob": "29/03/1998",
    "age": 24,
}

REGISTER_DATA_WITHOUT_DOB = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "gender": "Female",
    "age": 24,
}

REGISTER_DATA_WITHOUT_AGE = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "gender": "Female",
    "dob": "29/03/1998",
}

REGISTER_DATA_WITH_INVALID_EMAIL = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "ABCD",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "gender": "Female",
    "dob": "29/03/1998",
}

REGISTER_DATA_WITH_INVALID_PHONE_NUMBER = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681222",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Single",
    "gender": "Female",
    "dob": "29/03/1998",
    "age": 24,
}

REGISTER_DATA_WITH_INVALID_ZIPCODE = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568SDW345",
    "marital_status": "Single",
    "gender": "Female",
    "dob": "29/03/1998",
    "age": 24,
}

REGISTER_DATA_WITH_INVALID_MARITAL_STATUS = {
    "first_name": "test_name",
    "middle_name": "test_mid",
    "last_name": "test_last",
    "email": "test@gmail.com",
    "home_phone": "832-610-9681",
    "mobile_phone": "832-610-9681",
    "address_1": "test_palce",
    "address_2": "test_place",
    "city": "test_city",
    "state": "test_state",
    "zipcode": "77568",
    "marital_status": "Divorced",
    "gender": "Female",
    "dob": "29/03/1998",
    "age": 24,
}


@mock.patch("tasks.op_ticket_generator")
def test_new_registration(mock_queue):
    PatientData.drop_collection()
    patient_details = REGISTER_DATA
    PatientData(**patient_details).save()
    mock_queue.return_value = {
        "response": "Saved patient details successfully"
    }
    # when
    response = app.test_client().post(
        "/register",
        data=json.dumps(patient_details),
        content_type="application/json",
    )
    result = json.loads(response.data.decode())
    # then
    assert result["response"]
    assert response.status_code == 200


@mock.patch("tasks.op_ticket_generator")
def test_new_registration_without_body(mock_queue):
    with pytest.raises(ValidationError):
        PatientData.drop_collection()
        patient_details = {}
        PatientData(**patient_details).save()
        mock_queue.return_value = {"error": "request body not found"}
        # when
        response = app.test_client().post(
            "/register",
            data=json.dumps(patient_details),
            content_type="application/json",
        )
        # then
        assert response.status_code == 400


@pytest.mark.parametrize(
    "data",
    [
        REGISTER_DATA_WITHOUT_FIRTS_NAME,
        REGISTER_DATA_WITHOUT_LAST_NAME,
        REGISTER_DATAWITHOUT_ADDRESS_1,
        REGISTER_DATA_WITHOUT_GENDER,
        REGISTER_DATA_WITHOUT_DOB,
        REGISTER_DATA_WITHOUT_AGE,
    ],
)
@mock.patch("tasks.op_ticket_generator")
def test_new_registration_without_required_fields(mock_queue, data):
    with pytest.raises(ValidationError):
        PatientData.drop_collection()
        patient_details = data
        PatientData(**patient_details).save()
        mock_queue.return_value = {"message": "Unexpected error"}
        # when
        response = app.test_client().post(
            "/register",
            data=json.dumps(patient_details),
            content_type="application/json",
        )
        # then
        assert response.status_code == 500


@pytest.mark.parametrize(
    "data",
    [
        REGISTER_DATA_WITH_INVALID_EMAIL,
        REGISTER_DATA_WITH_INVALID_PHONE_NUMBER,
        REGISTER_DATA_WITH_INVALID_ZIPCODE,
        REGISTER_DATA_WITH_INVALID_MARITAL_STATUS,
    ],
)
@mock.patch("tasks.op_ticket_generator")
def test_new_registration_with_invalid_fields(mock_queue, data):
    with pytest.raises(ValidationError):
        PatientData.drop_collection()
        patient_details = data
        PatientData(**patient_details).save()
        mock_queue.return_value = {"message": "Unexpected error"}
        # when
        response = app.test_client().post(
            "/register",
            data=json.dumps(patient_details),
            content_type="application/json",
        )
        # then
        assert response.status_code == 500


@mock.patch("tasks.op_ticket_generator")
def test_get_patient_by_id(mock_queue):
    PatientData.drop_collection()
    patient_details = REGISTER_DATA
    patient = PatientData(**patient_details).save()
    json.loads(PatientData.objects.get(id=patient.id).to_json(indent=2))
    mock_queue.return_value = {"response": "Got patient details successfully"}
    # when
    response = app.test_client().get(
        f"/get_patient?Id={patient.id}", content_type="application/json"
    )
    result = json.loads(response.data.decode())
    # then
    assert result["response"]
    assert response.status_code == 200


@mock.patch("tasks.op_ticket_generator")
def test_get_patient_by_invalid_id(mock_queue):
    with pytest.raises(ValidationError):
        PatientData.drop_collection()
        patient_id = "INVALID_ID"
        mock_queue.return_value = {
            "response": "Got patient details successfully"
        }
        # when
        response = app.test_client().get(
            f"/get_patient?Id={patient_id}", content_type="application/json"
        )
        result = json.loads(response.data.decode())
        # then
        assert result["response"]
        assert response.status_code == 500
