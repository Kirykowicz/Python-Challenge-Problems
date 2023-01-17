import math 
import string

def vol(rad):
    return (4/3) * math.pi * rad**3

def ran_check(num, low, high):
    if num in range(low, high + 1):
        return f"{num} is in the range"
    else:
        return f'{num} is not in range'

def up_low(s):
    d = {"upper": 0, "lower":0}
    for char in s:
        if char.isupper():
            d['upper'] += 1
        if char.islower():
            d['lower'] += 1
    print("No. of Upper case characters : " + str(d['upper']))
    print("No. of Lower case characters : " + str(d['lower']))


def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def palindrome(s):
   s =  s.replace(' ', '')
   return s == s[::-1]
   
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str1 = str1.replace(' ', '')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset

