# Python If-Else

# Task 
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 <= n <= 100

# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.

#!/bin/python
import math
import os
import random
import re
import sys

def weird(n):
    if n%2==0 and n>0:
        if 2<=n<=5:
            print("Not Weird")
        elif 6<=n<=20:
            print("Weird")
        else: print("Not Weird")
    else: print("Weird")

if __name__ == '__main__':
    n = int(input().strip())
    weird(n)
