# <<<<<<<<<<<< DICTIONARY >>>>>>>>>>>>>>-------->

# pairs = (key : value)

marks = {'Ritu':52,'rohit':56,'rocky':53,'mohit':54}
# print(marks)
# print(type(marks))
# var['key']
# print(marks['mohit'])


# marks['rohit'] = 66  # Update the key value 
# print(marks)
# print(marks['rohit'])

# marks['rahul'] = 100   # insert an value or key 
print(marks)
print(marks.keys())
print(marks.values())

# marks.pop()
# print(marks)


# marks.pop('rohit')  # POP am key in the dict.
# print(marks)


# single variable = 5 student , names , marks , subject

students = {'Name':['rahul','mohit','ritu','yash','jugnu'],
            'Marks':[52,14,36,45,96],
            'Subject':"Science"}
print(students)
# print(type(students))
# print(students['Name'])
# print(students['Marks'])
# print(students['Subject'])


# students['Subject'] = "Physics"
# print(students['Subject'])

science_marks = {'Name':['rahul','mohit','ritu','yash','jugnu'],
            'Marks':[52,14,36,45,96],
            'Subject':"Science"}
print(science_marks)


#science_marks['Name'].remove('ritu')
#science_marks['Marks'].remove(36)

# science_marks['Name'].pop(2)
# science_marks['Marks'].pop(2)

# science_marks['Name'].insert('rishabh')
# science_marks['Marks'].insert(1,41)
# science_marks['Marks'][1] = 41

# print(science_marks)
# print(science_marks['Name']) 



# <<<<<<<<<<<<<< TYPE CASTING >>>>>>>>>>>>>>---->

# int() , float(), str(), tuple(), list(), set(), dict()

#num1 = 10
#num1 = float(num1)
#print(num1)
#print(type(num1))


#num2 = 10.78
#num2 = int(num2)
#print(num2)
#print(type(num2))


ls = [10,2,24,10,4,6,4,78,90,23,24,90,78,77,66]
# ls= set(ls) 
ls= list(set(ls))   # change set into list again
print(ls)




# <<<<<<<<<<<<<<<< OPERATORS >>>>>>>>>>----------->>>>

# ARITHMETIC Operation

# Addition          x + y
# Subtraction       x - y
# Multiplication    x * y
# Division          x / y
# Modulous          x % y
# Exponential       x ** y
# Floor Division    x // y

# 1. Arithmatic 

num1 = int(input(" Enter first number : "))
num2 = int(input(" Enter second number : "))

output1 = num1 + num2
print(output1)

output2 = num1 - num2
print(output2)

output3 = num1 * num2
print(output3)

output4 = num1 / num2
print(output4)

output5 = num1 % num2
print(output5)

output6 = num1 ** num2
print(output6)

output7 = num1 // num2
print(output7)



