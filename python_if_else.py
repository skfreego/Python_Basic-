"""
Task:- Given an Integer,n,perform the following conditional actions:
      . if n is odd,print Weird
      . if n is even and in the inclusive range of 2 to 5, print Not Weird
      . if n is even and in the inclusive range of 6 to 20, print Weird
      . if n is even and greater than 20, print Not Weird
Input Format:-  A single line containing a positive integer, n.
Output Format:-  Print Weird if the number is weird. Otherwise, print Not Weird.
"""

import math
import os
import random
import re
import sys

# if __name__ == '__main__':
#     n = int(input().strip())

n = 3
# n = 24

if n % 2 != 0:
    print("Weird")

else:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
