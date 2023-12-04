# Datr = 30-11-2023
'''
# WAP to display all keys and avalues of a dictionary

n = int(input())
dict_1 = {}
for i in range(n):
    key,value =  input().split()
    dict_1.update({key:value})
print(*dict_1.keys())
print(*dict_1.values())

'''

'''
# WAP to find the set bits of an integer using functions.
def set_bits(num):
    count = 0
    while num!=0:
        if num & 1 ==1:
            count+=1
        num = num>>1
    return count

n=int(input())
print(set_bits(n))

'''
'''
# Write a function that takes a list and returns a new list with unique elements of the first list and Repeated elements will be removed

def remove_duplicate(lst):
    lst1=set(lst)
    return list(lst1)

lst=[]
n=int(input())
for i in range(n):
    val = int(input())
    lst.append(val)

print(remove_duplicate(lst))
'''

# Write a functon to create and print a list where the values are square of numbers between 1 and n (both included)

def print_squares(n):
    lst=[]
    for i in range(n):
        lst.append((i+1)**2)
    return lst

n= int(input())
print(print_squares(n))