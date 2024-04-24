#!/bin/python3

import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    ret = 1
    while n>0:
       ret *= n
       n -= 1
    print(ret)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
