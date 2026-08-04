"""file = open("intro.txt" , 'x')
file.close()
with open("intro.txt" , 'w') as file:
    file.write(" i am tehmina , i am learning python")
"""
file = open("intro.txt" , 'r')
content = file.read()
print(content)

file.close()