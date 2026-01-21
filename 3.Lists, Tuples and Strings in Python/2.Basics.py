



# # ---------------------------------------------------List-----------------------------------------------

# names=["Aman",'Diwakar','Rahul','Priyanka']
# print(type(names))
# print(names[1])
# names[1]="Abhinav"
# print(names)
# b=[1555,"abcd",True, 1.23 ]
# print(b)

# a=[1,2,3,4,5,6,7,8,9,10]

# print(len(a))
# print(a[-2]) #-ve index
# print(a.append(b)) #take list as 1 single element
# print(a.extend(b)) #take element as different elemets 
# print(a.insert(3,100)) #(index,value-)-rest will shift 
# print(a.remove(1555)) #element
# print(a.pop(2)) #index--by default last element
# print(a.clear()) #remove all element


# print(min(a)) 
# print(max(a))
# print(a[2:6]) #slicing
# print(a.count(4)) #count specific element's appearence
# print(a.sort()) 
# print(a.reverse())

# list1 =a.copy() #shallow copy, original remains unchanged
# print(list)

# print(a.index(True)) #index of a specific element


# listOne=[1,2,3,4,5]
# print(listOne[::-1])  #reversing of list using slicing







#-----------------------------------------Tuple------------------------------------------------


# a=(1,2,3,4,5,"ABCD", True, 1.34)
# print(len(a))
# print(a[-2]) #-ve index
# print(min(a)) 
# print(max(a))
# print(a[2:6]) #slicing
# print(a.count(4)) #count specific element's appearence
# print(a.index(True)) #index of a specific element
 



#-----------------------------------------String------------------------------------------------




name = "abhinav"
grade = 'A'
company = "PW Skills"
introduction = """My name is Diwakar
I live in bangalore
I love coding"""

# print(type(name))
# print(type(grade))
# print(type(company))
# print(type(introduction))



a="#########Diwakar Nagar##############"
# print(a[2])
# print(a.upper())
# print(len(a))
# print(a[-1])
# print(a.lower())
# print(a.capitalize())
# print(a.replace("i","y"))
# print(a.count("a"))
# print(a.startswith("d"))
# print(a.endswith("Nagar"))
# print(a.find("i"))
# print(a.index("i"))
# print(a[2:5])

print(a.strip("#"))  #remove extra char at the ends

b="Hello my name is diwakar nagar"
print(b.split(" "))

list=['Hello', 'my', 'name', 'is', 'diwakar', 'nagar']
print(" ".join(list))

a='Diwakar Nagar'
print('Diwakar \n Nagar') #next line
print('Diwakar \t Nagar')  #tab-space
print(ord("A")) #ascii value