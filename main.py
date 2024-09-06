from src.logger import logging
from src.exception import CustomException


# List comprehension (Making doubled)
mylist_nums = [1, 2, 3, 4]
doubled = [x*2 for x in mylist_nums]
print(doubled)
logging.info("Numbers doubled successfully")

# List comprehension (Adding 2 in entire list)
numbers = [1,2,3,4,5,7]
add_two_numbers = [a+2 for a in numbers]
print(add_two_numbers)
logging.info("Numbers added 2 successfully")

# List comprehension (Squared)
mynumbs = [4, 6, 8]
squared = [x**2 for x in mynumbs]
print(f"Squared list is {squared}")
logging.info("Numbers list squared successfully")


## Iteration with List Comprehension
# using list comprehension to iterate by loop
list = [character for character in [1,2,3]]
print(list)


# Even list using List Comprehension
even_list = [i for i in range(11) if i % 2 == 0]
print(even_list)
logging.info("The even list is generated successfully.")


# Odd list using List Comprehension
odd_list = [i for i in range(12) if i % 2 == 1]
print(odd_list)
logging.info("The odd list is generated successfully.")




# List Comprehensions vs For Loop

mylist = []
for charater in 'Rohit':
    mylist.append(charater)

print(mylist)
logging.info("The mylist generated Successfully. Thank You.")