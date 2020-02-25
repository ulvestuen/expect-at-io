import requests
import json
import xmltodict
import flatten_dict


class WireMockResultChecker:
    body_type_handlers = {}

    def __init__(self):
        self.body_type_handlers["application/json"] = self.handler_json
        self.body_type_handlers["application/soap+xml"] = self.handler_xml
        self.body_type_handlers["application/xml"] = self.handler_xml
        self.body_type_handlers["text/xml"] = self.handler_xml

    def is_equal_to_expected(self, expected_result):
        wiremock_url = expected_result["mock_url"]
        body_type = expected_result["body_type"]
        expected_body_string = expected_result["body"]

        result_array = requests.get(wiremock_url).json()["requests"]
        if len(result_array) > 0:
            result_body_string = result_array[0]["request"]["body"]
            result_body = self.body_type_handlers[body_type](result_body_string)
            expected_body = self.body_type_handlers[body_type](expected_body_string)
            return self.is_equal_objects(flatten_dict.flatten(result_body, reducer="path"),
                                         flatten_dict.flatten(expected_body, reducer="path"))

    @staticmethod
    def reset_mock(expected_result):
        wiremock_url = expected_result["mock_url"]
        requests.delete(wiremock_url)

    @staticmethod
    def handler_json(body_string):
        return json.loads(body_string)

    @staticmethod
    def handler_xml(body_string):
        return xmltodict.parse(body_string)

    @staticmethod
    def is_equal_objects(actual, expected):
        is_equal = expected.keys() == actual.keys()

        for key in expected.keys():
            if expected[key] != "TO_BE_IGNORED":
                is_equal = is_equal and expected[key] == actual[key]

        return is_equal
