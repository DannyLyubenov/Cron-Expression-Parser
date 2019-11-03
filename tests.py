#!/usr/bin/env python3
import unittest
from prettytable import PrettyTable

# from main import main
from main import describe_cron

class MainUT(unittest.TestCase):
    
    def test_fields(self):
        # create table 1
        table = PrettyTable(["Field", "Description"])

        table.align["Field"] = "l"
        table.align["Description"] = "l"

        table.add_row(["minute", describe_cron("*/15",0,59)])
        table.add_row(["hour", describe_cron("0",0,23)])
        table.add_row(["day of month", describe_cron("1,15",1,31)])
        table.add_row(["month", describe_cron("*",1,12)])
        table.add_row(["day of week", describe_cron("1-5",0,6)])
        table.add_row(["command", "/usr/bin/find"])
  
        print(table)

        # create table 2
        table2 = PrettyTable(["Field", "Description"])

        table2.align["Field"] = "l"
        table2.align["Description"] = "l"

        table2.add_row(["minute", describe_cron("3-40",0,59)])
        table2.add_row(["hour", describe_cron("5",0,23)])
        table2.add_row(["day of month", describe_cron("2-20",1,31)])
        table2.add_row(["month", describe_cron("1-8",1,12)])
        table2.add_row(["day of week", describe_cron("*",0,6)])
        table2.add_row(["command", "/usr/bin/find"])
  
        print(table2)

        # create table 3
        table3 = PrettyTable(["Field", "Description"])

        table3.align["Field"] = "l"
        table3.align["Description"] = "l"

        table3.add_row(["minute", describe_cron("10,50",0,59)])
        table3.add_row(["hour", describe_cron("4-7",0,23)])
        table3.add_row(["day of month", describe_cron("*",1,31)])
        table3.add_row(["month", describe_cron("1,12",1,12)])
        table3.add_row(["day of week", describe_cron("5-6",0,6)])
        table3.add_row(["command", "/usr/bin/find"])
  
        print(table3)

        # create table 4
        table4 = PrettyTable(["Field", "Description"])

        table4.align["Field"] = "l"
        table4.align["Description"] = "l"

        table4.add_row(["minute", describe_cron("1-70",0,59)])
        table4.add_row(["hour", describe_cron("5",0,23)])
        table4.add_row(["day of month", describe_cron("2-20",1,31)])
        table4.add_row(["month", describe_cron("1-8",1,12)])
        table4.add_row(["day of week", describe_cron("*",0,6)])
        table4.add_row(["command", "/usr/bin/find"])
  
        print(table4)


if __name__ == '__main__':
   unittest.main()
