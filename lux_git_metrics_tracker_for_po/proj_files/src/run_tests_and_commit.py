import json
import subprocess
import sys

#epoch_time_for_nine_hours = 32400

class run_tests_and_commit_class():
    def __init__(self):
        with open('config.json') as config_file:
            config_data = json.load(config_file)

        print(config_data)
        self.path_to_tests = config_data["path_for_tests_to_run"]
    def run_tests_and_pipe_results_into_string(self):
        powershell_process = subprocess.Popen(["powershell.exe", 
              "py " + self.path_to_tests + " 2> test_results.txt"], 
              stdout=sys.stdout)
        powershell_process.communicate()
    def parse_test_result_file_for_pass_fail(self):
        with open('test_results.txt', 'r') as file:
            data = file.read().replace('\n', '')
        print(data.find('Rem'))

trial_run_object = run_tests_and_commit_class()
trial_run_object.run_tests_and_pipe_results_into_string()
trial_run_object.parse_test_result_file_for_pass_fail()
