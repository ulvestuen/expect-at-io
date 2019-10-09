import subprocess
import time
import threading


class TestService:
    ready_for_new_test = None
    collection = None
    test_data = None

    def __init__(self):
        self.ready_for_new_test = True

    @staticmethod
    def run_test():
        pid = subprocess.Popen(
            ["newman", "run", "-d", "http://localhost:5000/testdata", "http://localhost:5000/collection"]).pid
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
            if self.ready_for_new_test:
                continue_check = False
            if not self.ready_for_new_test:
                self.compare_result_with_expected()
            elif time.time() > start_time + max_wait:
                self.mark_test_failed()
                self.ready_for_new_test = True
                continue_check = False

    def compare_result_with_expected(self):
        print("Compare result with expected")
        self.ready_for_new_test = True

    def mark_test_failed(self):
        print("Test failed")
