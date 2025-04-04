# access the function of course_details from payment_details
import os , sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__),'..')))

from Course import course_details

def payment():
    print("This is my payment details")

course_details.course()

# if above is giving error (most likely due to a circular import), then delete/comment out both files cache from the left side and use below instructions
  # delete 2 lines from course_details.py
     # from Payment import payment_details    and     payment_details.payment()