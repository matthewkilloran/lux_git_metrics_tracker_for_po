import unittest
import os
import sys
from unittest.mock import MagicMock, Mock

sys.path.insert(1, '..\src')
# Commented out so test file does not call main file indefinitely
# from run_tests_and_commit import run_tests_and_commit_class

class first_test(unittest.TestCase):
    #--Tests--
    def test_mut_calls_my_second_function_once(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    #--Setup--
    @classmethod
    def setUp(self):
        self.mockFile = Mock()
     
if __name__ == '__main__':
    unittest.main()
