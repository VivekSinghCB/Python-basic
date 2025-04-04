# Modules and Import statements- A module in Python is a file that contains Python code (functions, classes, and variables). It allows code reuse and better organization.
    # Types- Build-in(math, random, os, sys, datetime, etc.), User defined, Third party(numpy, pandas, requests etc. )
# Importing can be done using import, from ... import, and aliasing (as). Use pip to install third-party modules

# e.g. our motive to access the function of payment_details from course_details and vice versa

#access the function of payment_details from course_details
import os , sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__),'..')))

from Payment import payment_details # press ctrl keep your cursor here to go to payment_details

def course():
    print("This is my course details")

payment_details.payment()
