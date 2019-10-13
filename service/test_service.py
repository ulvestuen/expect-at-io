import subprocess
import time
import threading
import requests
from service.wiremock_result_checker import WireMockResultChecker


class TestService:
    ready_for_new_test = None
    current_test_id = None
    collection = None
    input_data = None
    output_data = None

    result_checkers = {}

    def __init__(self):
        self.init()
        self.result_checkers["wiremock"] = WireMockResultChecker()

    def init(self):
        self.ready_for_new_test = True
        self.current_test_id = 0

    @staticmethod
    def run_test():
        pid = subprocess.Popen(
            ["newman", "run", "-d", "http://localhost:5000/inputdata", "http://localhost:5000/collection"]).pid
        return "Started newman with pid: " + str(pid)

    def run_check_for_result(self):
        t = threading.Thread(target=self.check_for_result)
        t.daemon = True
        t.start()

    def check_for_result(self):
        continue_check = True
        start_time = time.time()
        max_wait = 5
        while continue_check:
            print("Waiting 500 ms for next result check.")
            time.sleep(0.5)
            if not self.ready_for_new_test:
                self.compare_result_with_expected()
            if self.ready_for_new_test:
                continue_check = False
            elif time.time() > start_time + max_wait:
                self.mark_test_failed()
                self.get_ready_for_new_test()
                continue_check = False

    def compare_result_with_expected(self):
        print("Check results for test with id: " + str(self.current_test_id))
        result_check_list = self.get_result_check_list()
        all_results_ok = all([result_check["result_checker"].is_equal_to_expected(result_check["result"])
                              for result_check in result_check_list])

        if all_results_ok:
            print("Results checked OK for test with id: " + str(self.current_test_id))
            self.get_ready_for_new_test()

    def get_ready_for_new_test(self):
        result_check_list = self.get_result_check_list()
        for result_check in result_check_list:
            result_check["result_checker"].reset_mock(result_check["result"])
        self.current_test_id += 1
        self.ready_for_new_test = True

    def mark_test_failed(self):
        print("Results check failed for test with id: " + str(self.current_test_id))

    def get_result_check_list(self):
        expected_results = self.output_data[self.current_test_id]
        return [{"result_checker": self.result_checkers[result["mock_type"]], "result": result}
                for result in expected_results]
