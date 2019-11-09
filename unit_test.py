#!/usr/bin/env python3
import unittest
from main import describe_cron

class TestCases(unittest.TestCase):
    
    def test_step_value_fail(self):
        try:
            test_input = "*/15"
            result_list = []
            for i in range(0,60,10):
                result_list.append(i)
            
            # convert the list into string
            result_str = ' '.join(map(str, result_list))
            self.assertEqual(describe_cron(test_input,0,59),result_str)
        except Exception as e:
            print(e)

    def test_step_value_pass(self):
        try:
            test_input = "*/15"
            result_list = []
            for i in range(0,60,15):
                result_list.append(i)
            
            result_str = ' '.join(map(str, result_list))
            self.assertEqual(describe_cron(test_input,0,59),result_str)
        except Exception as e:
            print(e)

    def test_range_value_fail(self):
        try:
            test_input = "1-20"
            result_list = []
            for i in range(0,21):
                result_list.append(i)
            
            result_str = ' '.join(map(str, result_list))
            self.assertEqual(describe_cron(test_input,0,59),result_str)
        except Exception as e:
            print(e)

    def test_range_value_pass(self):
        try:
            test_input = "33-50"
            result_list = []
            for i in range(33,51):
                result_list.append(i)
            
            result_str = ' '.join(map(str, result_list))
            self.assertEqual(describe_cron(test_input,0,59),result_str)
        except Exception as e:
            print(e)

    def test_list_value_fail(self):
        try:
            test_input = "7,20"
            result_list = []

            for i in range(7,21):
                result_list.append(i)
            
            result_str = ' '.join(map(str, result_list))
            self.assertEqual(describe_cron(test_input,0,59),result_str)
        except Exception as e:
            print(e)

    def test_list_value_pass(self):
        try:
            test_input = "7,9"
            result_list = []
            split_str = test_input.split(",")

            for i in split_str:
                result_list.append(i)
            
            result_str = ' '.join(map(str, result_list))
            self.assertEqual(describe_cron(test_input,0,59),result_str)
        except Exception as e:
            print(e)

if __name__ == '__main__':
   unittest.main()
