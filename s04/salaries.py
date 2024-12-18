# SF Salaries Exercise

# Welcome to a quick exercise for you to practice your pandas skills! We will be using the SF Salaries Dataset from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**
import numpy as np
import pandas as pd

# ** Read Salaries.csv as a dataframe called sal.**

sal = pd.read_csv('./sf-salaries/Salaries.csv')

print(sal)

def get_headers(table):
  return list(table)

def get_info(table):
  return table.info()

def get_average_base_pay(table):
  return table['BasePay'].apply(pd.to_numeric, errors='coerce').mean()

def get_highest_amount_overtimepay(table):
  overtimePayMax = table['OvertimePay'].apply(pd.to_numeric, errors='coerce').max()
  print('OvertimePay {}'.format(overtimePayMax))
  return overtimePayMax

def get_employee_job_titble(table, employeeName):
  jobTitle = table[table['EmployeeName'] == employeeName]['JobTitle'].item()
  print('jobTitle {}'.format(jobTitle))
  return jobTitle

def get_employee_making_including_benefits(table, employeeName):
  total = table[table['EmployeeName'] == employeeName]['TotalPay'].item()
  print('{} total: {}'.format(employeeName, total))
  return total

def get_highest_paid_person_name(table):
  name = table[table['TotalPay'].max() == table['TotalPay']]['EmployeeName'].item()
  print('name: {}'.format(name))
  return name

def get_lowest_paid_person_name(table):
  name = table[table['TotalPay'].min() == table['TotalPay']]['EmployeeName'].item()
  print('name: {}'.format(name))
  return name

def get_average_basepay_of_all_employees_per_year(table):
  basePayAvg = table['BasePay'].groupby('Year').apply(pd.to_numeric, errors='coerce').mean()
  return basePayAvg

def what_are_the_top_5_most_common_jobs(table):
  top5 = table['JobTitle'].value_counts().head(5).index.tolist()
  print('top5: {}'.format(top5))
  return top5

def how_many_job_titles_were_represented_by_only_one_person_in_2013(table):
  # rows = table[table['Year'] == 2013].JobTitle.value_counts()
  rows = table.groupby('Year').JobTitle.nunique()
  print('count jobs: {}'.format(rows))
  return rows

