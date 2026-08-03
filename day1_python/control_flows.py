#sequential flow
print("Wake up")
print("Brush your teeth")
print("Go to university")

#decision making flow

age = 20

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

#looping flow

for i in range(5):
    print("This is iteration number:", i)


#while loop

count = 1
while count <= 5:
    print(count)
    count += 1

#jump statement

for i in range(10):
    if i == 5:
        break
    print(i)


#continue statement

for i in range(5):
    if i == 2:
        continue
    print(i)