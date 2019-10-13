import requests
import json


class WireMockResultChecker:
    body_type_handlers = {}

    def __init__(self):
        self.body_type_handlers["application/json"] = self.handler_json

    def is_equal_to_expected(self, expected_result):
        wiremock_url = expected_result["mock_url"]
        body_type = expected_result["body_type"]
        expected_body_string = expected_result["body"]

        result_array = requests.get(wiremock_url).json()["requests"]
        if len(result_array) > 0:
            result_body_string = result_array[0]["request"]["body"]
            result_body = self.body_type_handlers[body_type](result_body_string)
            expected_body = self.body_type_handlers[body_type](expected_body_string)
            print("Actual body:")
            print(result_body)
            print("Expected body:")
            print(expected_body)
            return result_body == expected_body

    @staticmethod
    def reset_mock(expected_result):
        wiremock_url = expected_result["mock_url"]
        requests.delete(wiremock_url)

    @staticmethod
    def handler_json(body_string):
        return json.loads(body_string)
