""" def greet():
    print("Hello Python")

greet()
greet()
greet()

def greet_user(name):
    print("hello " , name)

greet_user("John")
greet_user("Alice")
greet_user("Bob")  """

"""
#function of add numner
def add(num1, num2):
    return num1 + num2

number = add(10,20)
print(number)

#function of checking even number

def is_even():
    num = int(input())
    if num%2 == 0 :
        print("this is even number")
    else:
        print("this is odd number")

is_even()

#function of checking even number with parameter

def is_even(number):
    
    if number%2 == 0 :
        print("this is even number")
    else:
        print("this is odd number")

is_even(18)


"""

#function of checking largest number

def largest_num(num1 , num2 , num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
      return num3

largest = largest_num(18 , 20 ,30)
print(f"{largest} is greatest number")