import json
from flask import request, jsonify
from service.test_service import TestService

test_service = TestService()


def load():
    collection_file = request.files["collection"]
    io_data_file = request.files["testdata"]

    test_collection = json.load(collection_file)
    test_data = json.load(io_data_file)

    pre_request_event_index = [e["listen"] for e in test_collection["event"]].index("prerequest")
    pre_request_script = test_collection["event"][pre_request_event_index]["script"]["exec"]
    with open("resources/postman_pre-request.json", "r") as f:
        pre_request_script += json.load(f)

    test_service.init()
    test_service.collection = test_collection
    test_service.input_data = test_data["input"]
    test_service.output_data = test_data["output"]

    return "Test case loaded. Input data available at /spec/input \n" \
           "Expected output data available at /spec/output \n" \
           "Postman collection available at /spec/collection"


def run():
    return test_service.run_test()


def results():
    return jsonify(test_service.test_results)


def collection():
    return jsonify(test_service.collection)


def input_data():
    return jsonify(test_service.input_data)


def output_data():
    return jsonify(test_service.output_data)


def test_cases():
    api_request_names = [req["name"] for req in test_service.collection["item"]]
    test_case_list = []
    test_case_id = 0
    for input_data in test_service.input_data:
        for api_request in api_request_names:
            output_data_list = test_service.output_data[test_case_id]
            test_case = {"id": test_case_id,
                         "request": api_request,
                         "input": input_data,
                         "output": output_data_list}
            test_case_list.append(test_case)
            test_case_id += 1
    return jsonify(test_case_list)


def ready():
    return jsonify({"ready": test_service.ready_for_new_test})


def busy():
    test_service.ready_for_new_test = False
    test_service.run_check_for_result()
    return jsonify({"ready": test_service.ready_for_new_test})
