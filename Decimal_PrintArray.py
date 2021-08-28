#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):

    pos = 0
    neg = 0
    nopn = 0
    for i in range(0,len(arr)):
        if arr[i]>0:
            pos+=1
        elif arr[i]<0:
            neg+=1
        else:
           nopn+=1
            
   
    x=(pos+neg+nopn)
    value1 = pos/x
     
    print('%.6f'%value1)
    value2 = neg/x
    print('%.6f'%value2)
    value3 = nopn/x
    print('%.6f'%value3)
    
   
    
     

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
