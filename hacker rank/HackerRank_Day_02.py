'''
Problem 04
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
In the Gregorian calendar, three conditions are used to identify leap years:
    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

Task
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format

Read year, the year to test.

Constraints
1900<=year<=10^5

Output Format
The function must return a Boolean value (True/False). Output is handled by the provided code stub.
'''
#Code
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap=True
        if year % 100==0:
            leap = False
            if year % 400 ==0:
                leap =True
        
    return leap

year = int(input())
print(is_leap(year))

'''
Problem 05
The included code stub will read an integer, , from STDIN.Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.

Example
n=5
Print the string 12345.

Input Format
The first line contains an integer .

Constraints
1 <= n <= 150

Output Format
Print the list of integers from 1 through n as a string, without spaces.
'''
#Code
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1,end="")

'''
Problem 06
Task
You are given a string .
Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.

Input Format
A single line of input containing the string .

Constraints
 0 < len(S) < 100

Output Format
Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
'''
# Code 
import re
s = re.search(r"([a-zA-Z0-9])(\1)", input())
print(s.group(0)[0] if s else -1)