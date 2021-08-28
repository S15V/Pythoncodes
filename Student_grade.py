
import math
import os
import random
import re
import sys


def gradingStudents(grades):
    new_lst=[]
    for i in grades:
        if i % 5 < 2 or i<38:
            new_lst.append(i)
        else:
            new_lst.append(i+(5-(i % 5)))
    return new_lst

if __name__ == '__main__':

    grades = [33,83,69,92]
    result = gradingStudents(grades)

    for i in result:
        print(i)
