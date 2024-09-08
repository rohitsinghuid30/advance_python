import time
from src.logger import logging
from src.exception import CustomException
import sys

def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x
    


# print(attempt_float(1.21))
# print(attempt_float(1,21))
# print(attempt_float("Something"))



def myfloat(x:float)->float:
    try:
        return x
    except Exception as ex:
        raise CustomException(ex,sys)


print(myfloat(2,1))