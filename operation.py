a = 10
b = 3

print(a+b)     
print(a-b)
print(a*b)
print(a/b)  # 10 / 3 = 3.333...
print(a//b)  # 10 // 3 = 3 (floor division)
print(a%b)  # 10 % 3 = 1 (modulus)
print(a**b)  # 10 ** 3 = 1000

#comaprison operators
a = 5

print(a > 2) # a is greater than 2
print(a < 2) # a is less than 2
print(a == 5) # a is equal to 5
print(a != 5) # a is not equal to 5

#logical operators

age = 22

print(age > 18 and age < 30)
print(age > 18 or age < 10)
print(not True)

# assignment operators
x = 5

x += 3

print(x)  # x = 5 + 3 = 8
x -= 2
print(x)  # x = 8 - 2 = 6
x *= 5
print(x)  # x = 6 * 5 = 30
x /= 3
print(x)  # x = 30 / 3 = 10.0


#string operations

name = "Python"

print(name[0]) # it will print the first character of the string
print(name[-1]) # it will print the last character of the string
print(len(name)) # it will print the length of the string
print(name.upper()) # it will print the string in uppercase
print(name.lower()) # it will print the string in lowercase
print(name.replace("Python", "Java")) # it will replace "Python" with "Java" in the string