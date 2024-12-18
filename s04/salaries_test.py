import pytest
import pandas as pd
import salaries

# ** Check the head of the DataFrame. **
def test_get_headers():
  pd.testing.assert_series_equal(pd.Series(salaries.get_headers(salaries.sal)), pd.Series(['Id','EmployeeName','JobTitle','BasePay','OvertimePay','OtherPay','Benefits','TotalPay','TotalPayBenefits','Year','Notes','Agency','Status']))
  
# ** Use the .info() method to find out how many entries there are.**
def test_get_info():
  pd.testing.assert_series_equal(pd.Series(salaries.get_info(salaries.sal)), pd.Series(salaries.sal.info()))

# What is the average BasePay ?
def test_get_average_base_pay():
  assert salaries.get_average_base_pay(salaries.sal) == 66325.4488404877

# ** What is the highest amount of OvertimePay in the dataset ? **
def test_get_highest_amount_overtimepay():
  assert salaries.get_highest_amount_overtimepay(salaries.sal) == 245131.88

# ** What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **
def test_get_employee_job_titble():
  assert salaries.get_employee_job_titble(salaries.sal, 'JOSEPH DRISCOLL') == 'CAPTAIN, FIRE SUPPRESSION'

# ** How much does JOSEPH DRISCOLL make (including benefits)? **
def test_get_employee_making_including_benefits():
  assert salaries.get_employee_making_including_benefits(salaries.sal, 'JOSEPH DRISCOLL') == 270324.91

# ** What is the name of highest paid person (including benefits)?**
def test_get_highest_paid_person_name():
  assert salaries.get_highest_paid_person_name(salaries.sal) == 'NATHANIEL FORD'

# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**
def test_get_lowest_paid_person_name():
  assert salaries.get_lowest_paid_person_name(salaries.sal) == 'Joe Lopez'

# TODO fix this test
# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
# def test_get_average_basepay_of_all_employees_per_year():
#   pd.testing.assert_frame_equal(salaries.get_average_basepay_of_all_employees_per_year(salaries.sal), pd.DataFrame([63595.956517, 65436.406857, 69630.030216, 66564.421924], [2011, 2012, 2013, 2014]))

# ** What are the top 5 most common jobs? **
def test_what_are_the_top_5_most_common_jobs():
  assert salaries.what_are_the_top_5_most_common_jobs(salaries.sal) == ['Transit Operator', 'Special Nurse', 'Registered Nurse', 'Public Svc Aide-Public Works', 'Police Officer 3']

# Transit Operator                7036
# Special Nurse                   4389
# Registered Nurse                3736
# Public Svc Aide-Public Works    2518
# Police Officer 3                2421
# Name: JobTitle, dtype: int64

# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **
def test_how_many_job_titles_were_represented_by_only_one_person_in_2013():
  assert salaries.how_many_job_titles_were_represented_by_only_one_person_in_2013(salaries.sal) == 202

# 202

# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# 477

# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# title_len	TotalPayBenefits
# title_len	1.000000	-0.036878
# TotalPayBenefits	-0.036878	1.000000
