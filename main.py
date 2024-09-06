from src.logger import logging
from src.exception import CustomException


# List comprehension (Making doubled)
# mylist_nums = [1, 2, 3, 4]
# doubled = [x*2 for x in mylist_nums]
# print(doubled)
# logging.info("Numbers doubled successfully")

# # List comprehension (Adding 2 in entire list)
# numbers = [1,2,3,4,5,7]
# add_two_numbers = [a+2 for a in numbers]
# print(add_two_numbers)
# logging.info("Numbers added 2 successfully")

# List comprehension (Squared)
mynumbs = [4, 6, 8]
squared = [x**2 for x in mynumbs]
print(f"Squared list is {squared}")
logging.info("Numbers list squared successfully")