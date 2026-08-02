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

print(name[0])
print(name[-1])
print(len(name))
print(name.upper())
print(name.lower())
print(name.replace("Python", "Java"))