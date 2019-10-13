import requests
import json


class WireMockResultChecker:

    @staticmethod
    def is_equal_to_expected(expected_result):
        wiremock_url = expected_result["mock_url"]
        body_type = expected_result["body_type"]
        expected_body = expected_result["body"]

        result_array = requests.get(wiremock_url).json()["requests"]
        if len(result_array) > 0:
            result_body = result_array[0]["request"]["body"]
            # print("Actual body:")
            # print(result_body)
            # print("Expected body:")
            # print(expected_body)
            return result_body == expected_body

    @staticmethod
    def reset_mock(expected_result):
        wiremock_url = expected_result["mock_url"]
        requests.delete(wiremock_url)
