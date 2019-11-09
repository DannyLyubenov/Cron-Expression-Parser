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
  :return str cron_str: formatted user-friendly string
  """

  cron_list = []
  cron_str = ""
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
    valid_string(step_value[0],step_value[1],min_num,max_num)

    # convert back all the values to asterisk
    if(value_1_is_asterisk):
      step_value[0] = "*"
    if(value_2_is_asterisk):
      step_value[1] = "*"
    
    if(step_value[0] == "*"):
      for i in range(min_num,max_num+1,int(step_value[1])):        
        cron_list.append(i)
    else:
      for i in range(int(step_value[0]),max_num+1,int(step_value[1])):        
        cron_list.append(i)  

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

    valid_string(range_value[0],range_value[1],min_num,max_num)

    for i in range(int(range_value[0]),int(range_value[1])+1):      
      cron_list.append(i)

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

    valid_string(list_value[0],list_value[1],min_num,max_num)

    if(value_1_is_asterisk):
      list_value[0] = "*"
    if(value_2_is_asterisk):
      list_value[1] = "*"

    if(list_value[0] == "*"):
      for i in range(min_num,max_num+1):        
        cron_list.append(i)
    else:      
        cron_list.append(list_value[0])
    
    if(list_value[1] == "*"):
      for i in range(min_num,max_num+1):        
        cron_list.append(i)
    else:      
        cron_list.append(list_value[1])


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
          cron_list.append(i)
      else:

        # display only a single valid number
        cron_list.append(cron_field)
    else:
      print("ERROR: valid range " + "[" + str(min_num) + "-" + str(max_num) + "]")
      sys.exit()
  
  # convert list to string
  cron_str = ' '.join(map(str, cron_list))

  return cron_str    

def valid_string(num1, num2, min_num, max_num):
  """
    Error checking if the numbers are in range
  """
  if(int(num1) < min_num or int(num1) > max_num or int(num2) < min_num or int(num2) > max_num):
    print("ERROR: valid range " + "[" + str(min_num) + "-" + str(max_num) + "]")
    sys.exit()

if __name__=='__main__':
    main()