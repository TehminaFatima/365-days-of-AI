number = [1,2,3,4,5]
sq_number =[num**2 for num in number]
print(sq_number)

#copy list
cp_list = [num for num in number]
print(cp_list)

#doubel every number

db_num = [num*2 for num in number]
print(db_num)

#converting lowercase to upper case
name = ['ali' , 'ahemd'  , 'akber']
up_case = [nam.upper() for nam in name]
print(up_case)

#condition in comprehensions


#even number
even_number = [ num for num in number if num%2 == 0]
print(even_number)

#odd number
odd_number = [num for num in number if num%2 != 0]
print(odd_number)