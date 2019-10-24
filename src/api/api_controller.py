import json
from flask import request, jsonify


class ApiController:
    test_service = None

    def __init__(self, service):
        self.test_service = service

    def load(self):
        collection_file = request.files["collection"]
        io_data_file = request.files["testdata"]

        collection = json.load(collection_file)
        test_data = json.load(io_data_file)

        pre_request_event_index = [e["listen"] for e in collection["event"]].index("prerequest")
        pre_request_script = collection["event"][pre_request_event_index]["script"]["exec"]
        with open("resources/postman_pre-request.json", "r") as f:
            pre_request_script += json.load(f)

        self.test_service.init()
        self.test_service.collection = collection
        self.test_service.input_data = test_data["input"]
        self.test_service.output_data = test_data["output"]

        return "Test case loaded. Input data available at /inputdata \n" \
               "Expected output data available at /outputdata \n" \
               "Postman collection available at /collection"

    def run(self):
        return self.test_service.run_test()

    def results(self):
        return jsonify(self.test_service.test_results)

    def collection(self):
        return jsonify(self.test_service.collection)

    def input_data(self):
        return jsonify(self.test_service.input_data)

    def output_data(self):
        return jsonify(self.test_service.output_data)

    def ready(self):
        return jsonify({"ready": self.test_service.ready_for_new_test})

    def busy(self):
        self.test_service.ready_for_new_test = False
        self.test_service.run_check_for_result()
        return jsonify({"ready": self.test_service.ready_for_new_test})
