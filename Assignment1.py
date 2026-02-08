# Practice Questions :

#  Ques.1 Variable Swapping without Temporary Variable 
x = 10
y = 20
x, y = y, x
print((x , y))  

# Ques.2 List Slicing to Extract Elements 
numbers = [5, 8, 12, 15, 20, 25, 30, 35, 40, 45] 
first_three = numbers[:3] 
last_two = numbers[-2:]
print((first_three, last_two)) 

# Ques.3 Dictionary Key-Value Access 
marks = {"John": 85, "Emma": 92, "Liam": 78}
print((marks["John"], marks["Emma"])) 

# Ques.4 Tuple Unpacking 
data = (100, 200, 300, 400)
a,b,c,d = data 
print((a,b,c,d)) 

# Ques.5 Set Operations (Union & Intersection)
A = {1,2,3,4}
B = {3,4,5,6}
print((A | B , A & B)) 

# Ques.6 Dictionary update using Built-in Method 
person = {"name": "Alice", "city": "New York"}
person.update({"age": 25}) 
print(person) 


#Assignment-2
#Ques.1 
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())

L = [a,b,c,d,e,f,g,h]
print("List L:", L)
S = set(L) 
print("Set S:", S)  

# Ques.2
a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
g = input() 
h = input()

T = (a,b,c,d,e,f,g,h)
print("Tuple T:", T)

T_list = list(T)
new_value1 = input()
new_value2 = input()
T_list.append(new_value1)
T_list.append(new_value2)

T = tuple(T_list)
print("Updated Tuple T:", T)


