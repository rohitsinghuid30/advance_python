from src.logger import logging
import time


# nested comprehension list
matrix = []

for i in range(3):
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)

print(f"The Matrix is {matrix}")
logging.info(f"The matrix result is successfully.")


# nested list comprehension 3X3 Matrix
matrix = [[j for j in range(3)]for i in range(3)]