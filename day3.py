## <<<<---------BOOLEAN--------->>>>> ##
var1 = True
var2 = False

print(var1,var2)
print(type(var1),type(var2))

##  <<<<<<-------LIST---------->>>>>>> ##
# list has a dynamic array , static array and Referential
# static - size fixed (similar type array)
# dynamic - not fixed size (similar type array)
# Referential - both nature for python 

ls = [10,20,30,4,14,2.3,5.33 ,'upflairs',True]
print(ls)
print(type(ls))


# List have indexing 
ls1 = [34,22,12,22,34,55,1,23]
print(ls1[1])
print(ls1[0:2:4]) # print


ls2 = [10,20,14,2.3,5.33 ,'upflairs',True]
var = ls2[5]
print(var[4:7])


# mutable = changeable
# Immutable = unchangable
# student_name= ['taniya','yash','yash','prerna','ruchika','aditya','Ritu']
# student_name[0] = 'Tanya'


# student_name.append('Ritu')  # inserting in the last position

# student_name.pop()  # it remove the items from the last position


# student_name.insert(1,'gurpreet')  # not overrite but shift yash in 2 position

# student_name.remove('prerna') # it remove the items

# del student_name[2]  # it also remove an item by this method


# print(student_name)


# print(student_name.count('yash'))



# l1 =['A','B','C','D','E']
# l2 =[37,22,55,11,77,56,89,66,45]

# l1.reverse() # l1[::-1]
# l2.sort()  # assending order
# print(l2)
# l2.sort(reverse=True) # reverse the order
# print(l2)

# print(l2[::-1]) # it is also assending order
 
# print(max(l2))
# print(sum(l2))
# print(min(l2))



# Concatinate ------->>>>>


# l1 =['A','B','C','D','E']
# l2 =[37,22,55,11,77,56,89,66,45]
#full_list = l1 + l2
#print(l1+l2)
#print(full_list)

#l1.append(l2) # put the list as it is
# l1.extend(l2)  # first extend the list then combine it
#print(l1)

# print(l1.index('C'))


list1 = [10,20,3.1,'upflairs pvt ltd',500,400]
list1[2]=100
print(list1)
list1.insert(3,'upflair')
print(list1)


# <<<<---------------TUPLE --------------------->>>>
# imutable 
# tuples are only make at once time and not changable
# Hetrogeneous datatypes


tpl = (25,41,63,96,'upflairs',True,25.2)
# del tpl[4] # not use for tuple 
# print(tpl)
#print(tpl[4])

# print(type(tpl))

#tpl[4] = 'flipcart'
#print(tpl)
#tpl.count()
#tpl.index()




# <<<<<<<<<<<<<<< SETS >>>>>>>>>>>>>> ----->
# sets doesn't allow duplicates datatypes
# unordered data

# set = {56,24,1,26,34,55,23,55,78,66,90,22,2,3,90}
# print(set[2])


# set.add(500)

# set.remove(55)
# set.remove(550)
# set.discard(550) # it also remove the item and don't show error

# print(set)
#print(type(set))



# st1 = {52,34,78,90,45,76}
# st2 = {34,78,66,90,56,23}

# print(st1+st2)
# st1.update(st2)  # it add st1 + st2 
# print(st1)
# print(st1.intersection(st2))





# <<<<<<<<<<<< DICTIONARY >>>>>>>>>>>>>>-------->

# pairs = (key : value)

marks = {'mohit':52,'rohit':56,'rocky':53,'mohit':54}
print(marks)
print(type(marks))
