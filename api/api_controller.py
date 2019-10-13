from flask import request, jsonify
import json


class ApiController:
    test_service = None

    def __init__(self, service):
        self.test_service = service

    def run(self):
        collection_file = request.files["collection"]
        io_data_file = request.files["testdata"]

        collection = json.load(collection_file)
        test_data = json.load(io_data_file)

        self.test_service.init()
        self.test_service.collection = collection
        self.test_service.input_data = test_data["input"]
        self.test_service.output_data = test_data["output"]

        return self.test_service.run_test()

    def collection(self):
        return jsonify(self.test_service.collection)

    def input_data(self):
        return jsonify(self.test_service.input_data)

    def ready(self):
        return jsonify({"ready": self.test_service.ready_for_new_test})

    def busy(self):
        self.test_service.ready_for_new_test = False
        self.test_service.run_check_for_result()
        return jsonify({"ready": self.test_service.ready_for_new_test})
