#program to find user senior citizen or not

from datetime import date
#it is a python module used to work with date and times

name = input('enter your name:')
DOB = int(input('enter your birth date:'))

currentyear = date.today().year
age = currentyear - DOB
# .year extracts  only the year then simple calculation


if age>60:
    print(name,'is a sinor citizen')
else:
    print(name,'is not a senior citizen')