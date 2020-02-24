import time


class AuxillaryModules:
    @staticmethod
    def job_hold(time_interval):
        time.sleep(time_interval)


class TestResults:
    def __init__(self, total):
        self.__passed = 0
        self.__failed = 0
        self.total = total

    def pass_result_update(self):
        self.__passed = self.__passed + 1

    def fail_result_update(self):
        self.__failed = self.__failed + 1

    def print_result(self):
        print('================================================================================')
        print("Suite")
        print(f'Total tests run: {self.total}, Failures: {self.__failed}, Passed:{self.__passed}')
        print('================================================================================')
