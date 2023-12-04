'''Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 , print Not Weird
If n is even and in the inclusive range of 6 to 20 , print Weird
If n is even and greater than 20 , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.'''

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif n%2==0:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")

'''
Task
The provided code stub reads two integers from STDIN, a and b . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.


Print the following:

8
-2
15
Input Format

The first line contains the first integer, .
The second line contains the second integer, .


Output Format

Print the three lines as explained above.
'''

if __name__ == '__main__':
    a = int(input(""))
    b = int(input(""))
    sum_ = a+b
    diff = a-b
    prod = a*b
    print(sum_)
    print(diff)
    print(prod)
'''
Task
The provided code stub reads two integers, a and b  , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a // b . The second line should contain the result of float division, a / b .

No rounding or formatting is necessary.
'''
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    in_div = a//b
    fl_div = a/b
    print(in_div)
    print(fl_div)
    
