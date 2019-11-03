#!/usr/bin/env python3
"""
  Usage: main.py <minute> <hour> <day_of_month> <month> <day_of_week> <command>
"""
from docopt import docopt
from prettytable import PrettyTable
import sys

def main():
  args = docopt(__doc__, version='0.1')

  # read all perameters and store them in variables 
  minute = args['<minute>'] 
  hour = args["<hour>"]
  day_of_month = args["<day_of_month>"]
  month = args["<month>"]
  day_of_week = args["<day_of_week>"]
  command = args["<command>"]
  
  # create table
  table = PrettyTable(["Field", "Description"])

  # left justify the table fields
  table.align["Field"] = "l"
  table.align["Description"] = "l"

  # create each row
  table.add_row(["minute", describe_cron(minute,0,59)])
  table.add_row(["hour", describe_cron(hour,0,23)])
  table.add_row(["day of month", describe_cron(day_of_month,1,31)])
  table.add_row(["month", describe_cron(month,1,12)])
  table.add_row(["day of week", describe_cron(day_of_week,0,6)])
  table.add_row(["command", command])
  
  print(table)


def describe_cron(cron_field,min_num,max_num):
  """
  Convert a cron expression into numbers

  :param str cron_field: individual crontab field
  :param int min_num: the minimum value associated with each field
  :param int max_num: the maximum value associated with each field
  :return str describe_cron_string: formatted user-friendly string
  """

  describe_cron_string = ""
  #------ Step Value ------ 
  if("/" in cron_field):
    step_value = cron_field.split("/")
    value_1_is_asterisk = False
    value_2_is_asterisk = False

    # convert value 1 and value 2 into a valid number to pass the error check
    if(step_value[0] == "*"):
      step_value[0] = "1"
      value_1_is_asterisk = True  
    if(step_value[1] == "*"):
      step_value[1] = "1"
      value_2_is_asterisk = True

    # error check if values are in a valid range
    if(int(step_value[0]) < min_num or int(step_value[0]) > max_num or int(step_value[1]) < min_num or int(step_value[1]) > max_num):
      print("ERROR: valid range " + "[" + str(min_num) + "-" + str(max_num) + "]")
      sys.exit()

    # convert back all the values to asterisk
    if(value_1_is_asterisk):
      step_value[0] = "*"
    if(value_2_is_asterisk):
      step_value[1] = "*"
    
    if(step_value[0] == "*"):
      for i in range(min_num,max_num+1,int(step_value[1])):
        describe_cron_string += str(i) + " "  
    else:
      for i in range(int(step_value[0]),max_num+1,int(step_value[1])):
        describe_cron_string += str(i) + " "   

  #------ Range Value ------
  elif("-" in cron_field):
    range_value = cron_field.split("-")
    value_1_is_asterisk = False
    value_2_is_asterisk = False

    # convert the values into an invalid number 
    # asterisk is not allowed in range
    if(range_value[0] == "*"):
      range_value[0] = "100"
      value_1_is_asterisk = True  
    if(range_value[1] == "*"):
      range_value[1] = "100"
      value_2_is_asterisk = True

    if(int(range_value[0]) < min_num or int(range_value[0]) > max_num or int(range_value[1]) < min_num or int(range_value[1]) > max_num):
      print("ERROR: valid range " + "[" + str(min_num) + "-" + str(max_num) + "]")
      sys.exit()

    for i in range(int(range_value[0]),int(range_value[1])+1):
      describe_cron_string += str(i) + " "

  #------ Value List Separator ------
  elif("," in cron_field):
    list_value = cron_field.split(",")
    value_1_is_asterisk = False
    value_2_is_asterisk = False

    if(list_value[0] == "*"):
      list_value[0] = "1"
      value_1_is_asterisk = True  
    if(list_value[1] == "*"):
      list_value[1] = "1"
      value_2_is_asterisk = True

    if(int(list_value[0]) < min_num or int(list_value[0]) > max_num or int(list_value[1]) < min_num or int(list_value[1]) > max_num):
      print("ERROR: valid range " + "[" + str(min_num) + "-" + str(max_num) + "]")
      sys.exit()

    if(value_1_is_asterisk):
      list_value[0] = "*"
    if(value_2_is_asterisk):
      list_value[1] = "*"

    if(list_value[0] == "*"):
      for i in range(min_num,max_num+1):
        describe_cron_string += str(i) + " "
    else:
      describe_cron_string += str(list_value[0]) + " "
    
    if(list_value[1] == "*"):
      for i in range(min_num,max_num+1):
        describe_cron_string += str(i) + " "
    else:
      describe_cron_string += str(list_value[1]) + " "

  #------ Regular Numbers ------
  else:
    value_1_is_asterisk = False

    if(cron_field == "*"):
      cron_field = "1"
      value_1_is_asterisk = True 

    if(int(cron_field) >= min_num and int(cron_field) <= max_num):
      
      # display all numbers if asterisk is used
      if(value_1_is_asterisk):
        for i in range(min_num,max_num+1):
          describe_cron_string += str(i) + " "
      else:

        # display only a single valid number
        describe_cron_string = cron_field
    else:
      print("ERROR: valid range " + "[" + str(min_num) + "-" + str(max_num) + "]")
      sys.exit()
      
  return describe_cron_string    


if __name__=='__main__':
    main()