x = 3
y = 7
x,y = y,x
print("x=", x)
print("y=", y) 

name1 = "Alice"
name2 = "Bob"
name1,name2 = name2, name1
print("name1=", name1)
print("name2=", name2) 

m = input()
n = input()
temp = m
m = n 
n = temp
print("m=", m)
print("n=", n)  

x =float(input()) 
y = int(x)
print(y) 

str = "42"
num = int(str)
print(num) 

str = "Hello"
q = list(str)
print(q) 
r = tuple(str)
print(r) 
p = set(str)
print(p) 
print(type(q))
print(type(p)) 
print(type(r))  

a = int(input())
b = int(input())
print(a + b) #14
print(a - b) # 10
print(a * b) # 24
print(a ** b) # 144
print(a / b)  # 6.0
print(a // b)  # 6
print(a % b)  # 0  

a = True 
b = False
print( a and b )
print( a or  b )
print(not a)
print(not b)

a = 10
a += 5
print(a)
a*= 2
print(a)

a =int(input())
b = int(input())
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(~b)
print(a>>1)
print(a<<1)

a = int(input())
b = int(input())
print(a % b)

a = 7 > 3
b = 4 < 2 
c = 5==5
print( a and b or c)  

X = ['apple', 'banana']
Y = ['apple', 'banana']
print(X==Y)
print(X is Y)

X = ['apple', 'banana']
Y = ['apple', 'banana']
print(X is Y)
Z = X 
print( Z is X ) 

age = 20 
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible ")


num = int(input())
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is odd") 

year = int(input())
if year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("not a leap year")

items = [1,2,3]
if items == [1,2,3]:
    print("Items is not empty")
else:
    print("Items is empty")

marks = int(input())
if 0 < marks < 100:
    print("valid range")
else:
    print("not a valid range")

age = 2
has_id = False 
if age >= 18:
    if has_id:
        print("u can enter")
    else:
        print("bring your id and then go")
else:
    print("sorry, u can't enter")

score = 120
if 0 < score < 100:
    if score > 40:
        print("pass")
    else:
        print("failed")
else:
    print("not valid")  

num1 = int(input())
last_digit = num1 % 10
if last_digit % 2 == 0:
    print("Last digit is even")
else:
    print("Last digit is odd") 



l = [11,22,33,44,55,66,77,88,99]
for i in l:
    if (i < 66):
        print(i)
    else:
        print(i + 1)

l = [12,20,33,4,5,26,7,84,96]
for i in l:
    f=0
    for j in range(2, i):
        if (i%j==0):
            f=1
    if f==0:
        print(i)    # prints prime number from list l
print(len(l))


l = [12,20,33,4,5,26,7,84,96,101,12,4]
n = len(l)
x = int(input())
print(n)
for i in range(n):
    if x==l[i]:
        print(i)
    print(i, l[i]) 

l = [47,83,74,90,83,24,74,100,64,67,100,47,90]
max = 0
for i in l:
    if i > max:
        max = i 
       
n = len(l)
for j in range(n):
    if l[j] == max:
        print(j) 
print(max)   # code to print the max and at which index using for loop 



n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)
print(l) 
a = int(input())
b = int(input())
k = len(l)
for i in range(k):
    if (l[i]==a):
        l[i]= b 
print(l)  

L1 = [11,22,33,22,44]
L2 = [13,22,11,14,43]
L3 =[]
for i in L1:
    if (i not in L3):
        L3.append(i)
for i in L2:
    if (i not in L3):
        L3.append(i)
print(L3)   

for i in L1:
    if (i % 2 == 0):
        if (i not in L3):
            L3.append(i)

for i in L2:
    if (i % 2 == 0):
        if (i not in L3):
            L3.append(i) 
print(L3) 



day = "Tuesday"
match day:
    case "Monday":
        print("Start of the week")
    case "Sunday":
        print("End of the week")
    case _:
        print("Working days")

a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print("a is greatest")
elif b >= a and b >= c:
    print("b is greatest")
else:
    print("c is greatest") 

a = int(input())
b = int(input())
c = int(input())
result = max(a,b,c)
print(result)

students = ["aarav", "anuj", "manav"]
for student in students:
    print("Hello", student) 

for i in range(1,6):
    print("Roll no." , i)

cities = ["mumbai", "delhi", "UP", "MP", "AP"]
for city in cities:
    if city == "UP":
        continue
    print(city)  

names = ["anuj", "aman", "ankit", "ankur", "anant"]
for name in names:
    if name == "ankit":
        break
    print(name) 

for item in ["tea", "coffee", "milk", "juice", "water"]:
    print("serving", item)
else:
    print("All drinks served!")

students = ["anuj", "aman", "ankit"]
subjects = ["maths", "science", "GK"]
for student in students:
    for subject in subjects:
        print(f"{student} , is studying , {subject}") 

for i in range(0,6):
    print(i)

num = 0
while num < 5:
    num += 1
    print(num) 

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
 
n = int(input())
total = 0
for i in range(1, n+1):
    total += i
print(total) 

count = 1
while count < 6:
    print(count)
    count += 1 

count = 2
while count < 11:
    print(count)
    count += 2 

num = 1232
count = 0
while num > 0:
    num //= 10
    count += 1
print(count) 

loops = ["l", "o", "o", "p"]
for loop in loops:
    print(loop)

for i in range(1,11,2):
    print(i) 

for i in range(0, 11, 3):
    print(i)  

for i in range(0,21,4):
    print(i)

sum = 0
for i in range(1,7):
    sum += i
print(sum) 


words = "Aayuesh"
vowels = "aeiouAEIOU"
count = 0
for letter in words:
    if letter in vowels:
        count += 1
print(count)  
 

for num in range(1,7):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


for i in range(1, 11):
    for j in range(1,11):
        product = i * j
        print(f"{i}*{j}={product}")
print() 


vowels = "aeiouAEIOU"
for letter in "sunshine":
    if letter not in vowels:
        continue 
    print(letter)   


vowels = "aeiouAEIOU"
for letter in "redmoon":
    if letter not in vowels: 
        continue
    print(letter)  


total = 0
for number in range(2,9,2):
    total += number 
print(total) 


total = 0
for number in range(1,10,2):
    if number % 2 != 0:
        total += number
print(total) 


vowels="AEIOUaeiou"
for letter in "python":
    if letter in vowels:
        continue
    print(letter)


year = int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not leap year") 


n = int(input())
for i in range(1,n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print() 


n = int(input())
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j , end=" ")
    print() 


n = int(input())
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i  , end=" ")
    print() 


n = int(input())
for i in range(1,n+1):
    for j in range(1, n+1):
        print(i*j , end=" ")
    print() 


n = int(input())
for i in range(1,n+1):
    s = n-i 
    for k  in range(1, s+1):
        print(" " , end="")
    for j in range(1, i+1):
        print("*" , end="")
    print()   


n = int(input())
for i in range(1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))
print() 


#armstrong pattern in python 


# Functions :-
a = int(input())
b = int(input())
def add(c,d):
    return(c+d)
def sub(c,d):
    return(c-d)
def mlt(c,d):
    return(c*d)
def div(c,d):
    return(c/d)
print(add(a,b))
print(sub(a,b))
print(mlt(a,b))
print(div(a,b))

 
a = int(input())
b = int(input())
for i in range(a, b+1):
    for j in range(1,11):
        print(i, "*", j, "=", i*j)
    print("***********************************") 


a = int(input())
b = int(input())
def lin():
    for i in range(50):
        print("*", end="") 
    print() 
for i in range(a, b+1):
    for j in range(1,11):
        print(i, "*", j, "=", i*j)
    lin()
 
for i in range(2,6):
    for j in range(1,9):
        product = i * j
        print(f"{i}*{j}={product}")
print()    
   


def tbl(a,b,c=1,d=8):
    for i in range(a,b+1):
        for j in range(c,d+1):
            print(i, "*", j , "=", i*j) 
        print("***************************************")  
x = int(input())
y = int(input())
tbl(x,y)  


def rev(n):
    r = 0 
    k = n 
    while (k>0):
        r = r*10+(k%10) 
        k = k//10 
    print(r) 
a = int(input()) 
rev(a) 



# check if a number is prime or not : 
num = int(input())
is_prime = True 
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break 
if is_prime and num>1:
    print(num, "is a prime number")
else:
    print(num , "is not a prime number")  



# count outcomes of each string:
word = "programming" 
char_count = {}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char , count in char_count.items():
    print(char+ ':' , count)   


# printing n natural numbers in a single line 
for i in range(1,6):
    print(i, end=" ")


# printing the squares of the numbers in range 
for i in range(1,6):
    print(i**2, end=" ")


# printing the even numbers in a particular range 
for i in range(1,6):
    if i%2==0:
        print(i, end=" ") 


# sum upto n natural numbers 
total = 0
for i in range(1,11):
    total+=i 
print(total)  


#printing the reverse of the word 
word = "python" 
for i in range(len(word) -1 , -1, -1):
    print(word[i], end="") 


# counting the number of vowels 
vowels = "aeiou" 
word = "education"  # vowels are 5 
count = 0 
for char in word:
    if char in vowels:
        count+=1 
print(count)  


#fibonacci series 
a = 0
b = 1
print(a,b,end=" ")
for i in range(8):
    next_term = a+b
    print(next_term, end=" ")
    a,b = b,next_term 


# factorial of a number 
n = 5
factorial = 1
for i in range(1, n+1):
    factorial*=i 
print(factorial) 


#  armstrong 
num = int(input())
original_num = num 
digits = len(str(num))
sum_of_powers = 0
while num>0:
    f = num%10 
    sum_of_powers += f**digits 
    num //= 10
if original_num == sum_of_powers:
    print(f"{original_num} is an armstrong") 
else:
    print(f"{original_num} is not an armstrong")   

length = float(input())
area = 6*(length**2)
result = float(f"{area:.2f}")
print(result)


NEW_RENTAL = 3.00
OLDIE_RENTAL = 2.00
NEW_VIDEOS = int(input())
OLDIE_VIDEOS = int(input())
result = (NEW_RENTAL*NEW_VIDEOS) + (OLDIE_RENTAL*OLDIE_VIDEOS)
print(f"{result:.2f}")


initial_height = float(input())
no_of_weeks = int(input())
growth_per = 0.5 
result = growth_per*no_of_weeks
final = result + initial_height
print(final)  


initial = int(input())
rate = float(input())
hours = int(input())
total_hours = int(input())
no_of_growth_cycles = total_hours // hours 
final = initial*(rate**no_of_growth_cycles)
print(int(final))  


salary = float(input())
gender = input() 
if gender=="M":
    bonus_percent = 0.05
elif gender=="F":
    bonus_percent = 0.10
else:
    bonus_percent = 0
if salary<10000:
    bonus_percent+=0.02 
bonus_amount = salary*bonus_percent 
total = bonus_amount + salary 
print(f"{bonus_amount:.2f}")
print(f"{total:.2f}")  


economy = int(input())
cost_of_economy = int(input()) 
position = int(input()) 
if position<=economy:
    amount = cost_of_economy
else:
    vip = (position-economy-1)*5
    amount = cost_of_economy + vip +5
print(amount) 

n = int(input()) 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 


number = input() 
for digit in number:
    print(digit)   


# Take input from the user (assuming valid integer input)
number_str = input("Enter an integer to check if it's a Perfect Number: ")
number = int(number_str) # This will raise a ValueError if input is not an integer
# Handle cases where the input is less than 1
if number <= 0:
    print("Perfect numbers are positive integers. Please enter a positive integer.")
else:
    sum_of_divisors = 0
    # Iterate from 1 up to number-1 to find proper divisors
    for i in range(1, number):
        if number % i == 0:  # If 'i' is a divisor of 'number'
            sum_of_divisors += i  # Add it to the sum
print(number) 
    #  Check if the sum of divisors equals the original number
if sum_of_divisors == number:
    print(f"{number} is a Perfect Number.")
else:
    print(f"{number} is not a Perfect Number.")   


n = int(input()) 
for i in range(2,n):
    if(n%i)==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")   


def helloWorld():
    print("Good Morning") 
    print("Have Breakfast") 
    print("Go to School") 
helloWorld() 


def find_char(str1, char):
    if char in str1:
        return str1.index(char)
    else:
        return "not found" 
a = input()
b = input()
print(find_char(a,b))

def max_of_three(x,y,z):
    if x>y and y>z:
        return x
    elif y>z:
        return y
    else:
        return z
x = int(input())
y = int(input()) 
z = int(input())  
print(max_of_three(x,y,z))

def Intro():
    print("Welcome to python programming")
Intro()

def Lang():
    print("Python is a high-level language")
Lang()

def find_char(str1, char):
    for i,c in enumerate(str1):
        if c==char:
            return i+1
    return "not found"
a = input()
b = input()
print(find_char(a,b)) 

def And(x,y):                                    
    return x&y
def Or(x,y):
    return x|y
def Xor(x,y):
    return x^y

x = int(input()) 
y = int(input()) 
print(And(x,y))
print(Or(x,y))
print(Xor(x,y))

def helloworld():
    print("Hello World")
    print("Good Morning")
    print("Have a nice day")
    print("The function ends") 
helloworld()

def addavg(a,b):
    return a+b, a+b/2
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

a = int(input()) 
b = int(input()) 
print(addavg(a,b))
print(sub(a,b))
print(mul(a,b))

d = int(input()) 
e = int(input()) 
def add(a,b):
    return a+b 
x = add(d,e)
print(x) 

def nameage(*,name,age):
    print(f"{name} {age}")
    print(name,age)
name = input()
age = int(input())
nameage(name=name, age=age) 

def time_to_minutes(hours, minutes):
    total_minutes = (hours*60) + minutes
    return total_minutes
hours = int(input()) 
minutes = int(input())
print(time_to_minutes(hours, minutes)) 

def odd_ind(str1):
    return str1[1::2]
if __name__ == "__main__":
    input_string = input()
    print(odd_ind(input_string)) 

def verify(*,a,b,c):
    if a%2==0 and b%2!=0 and c%2!=0:
        return a+b+c
    elif a%2!=0 and b%2==0 and c%2==0:
        return a*b*c
    else:
        return "Invalid"
    
a = int(input()) 
b = int(input()) 
c = int(input()) 
print(verify(a=a,b=b,c=c))

def my_min(*args):
    return min(args)
if __name__ == "__main__":
    a = int(input())
    b = int(input()) 
    c = int(input()) 
    d = int(input()) 
    e = int(input()) 
print(my_min(a,b,c,d,e))

def mySum(*args):
    total = sum(args)
    return total
a = int(input()) 
b = int(input()) 
c = int(input()) 
d = int(input()) 
print(mySum(a,b,c,d))
print(mySum(a,b,c))
print(mySum(a,b))
print(mySum(a))

doublenum = lambda x: x*2
a = int(input()) 
print(doublenum(a))
doublenum(a) 

square = lambda x: x**2
a = int(input()) 
print(square(a))
square(a) 

increment_by_one = lambda x: x+1
a = int(input()) 
print(increment_by_one(a))
increment_by_one(a) 

def squares(x):
    return x**2
list1 = list(map(int, input().split(",")))
print(list(map(squares, list1))) 

a = list(map(int,input().split(",")))
print(list(filter(lambda x: x%2==0, a))) 

momentum = lambda mass, velocity: mass*velocity
mass = float(input()) 
velocity = float(input())
result = momentum(mass,velocity)
print(f"{result:.2f}")

product = lambda x,y: x*y
x = int(input()) 
y = int(input()) 
result = product(x,y)
print(f"{result:.2f}") 

force = lambda mass,acc: mass*acc
mass = float(input()) 
acc = float(input()) 
result = force(mass,acc)
print(f"{result:.2f}")

sqaure_root = lambda x: x**0.5
n = int(input()) 
print(f"{sqaure_root(n):.2f}") 

r = lambda x: x+15
print(r(int(input())))

alph = lambda alph: chr(ord(alph)-1)
print(alph(input()))  

def find_char(str1,char):
    if char in str1:
        return str1.index(char)
    else:
        return "not found"
a = (input())
b = (input())
print(find_char(a,b))

def Intro():
    print("Welcome to python programming.")
Intro()

def Lang():
    print("Python is a middle level language.")
Lang() 

def max_of_three(x,y,z):
    if x > y or y > z:
        return x 
    elif y > z:
        return y
    else:
        return z
x = int(input())
y = int(input())
z = int(input()) 
print(max_of_three(x,y,z))

def find_char(str1,char):
    for i,c in enumerate(str1):
        if c==char:
            return i+1
    return "not found"
a = input()
b = input()
print(find_char(a,b))

def And(x,y):
    return x&y
def Or(x,y):
    return x|y
def Xor(x,y):
    return x^y
x = int(input())
y = int(input())
print(And(x,y))
print(Or(x,y))
print(Xor(x,y))

def helloWorld():
    print("Hello World")
    print("Good Morning")
    print("Have a nice day")
    print("The function ends")
helloWorld()

def addavg(x,y):
    return x+y, (x+y)/2
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y

a = int(input())
b = int(input())
print(addavg(a,b))
print(sub(a,b))
print(mul(a,b))  

d = int(input())
e = int(input()) 
def add(a,b):
    return a+b
x = add(d,e)
print(x) 

def time_to_minutes(hours,minutes):
    result = (hours*60) + minutes
    return result
hours = int(input())
minutes = int(input())
result = time_to_minutes(hours,minutes)
print(result) 

def verify(a,b,c):
    if a%2==0 and b%2==0 and c%2==0:
        return a*b*c
    elif a%2!=0 and b%2!=0 and c%2!=0:
        return a+b+c
    else:
        return "invalid"
a = int(input())
b = int(input())
c = int(input())
print(verify(a,b,c)) 

def mySum(*arg):
    total = sum(arg)
    return total
a = int(input()) 
b = int(input()) 
c = int(input()) 
d = int(input()) 
print(mySum(a,b,c,d))
print(mySum(a,b,c))
print(mySum(a,b))

doublenum = lambda x: x*2
a = int(input())
print(doublenum(a))
doublenum(a) 

def squares(x):
    return x**2
list1 = list(map(int,input().split(",")))
print(list(map(squares, list1))) 

a = list(map(int,input().split(",")))
print(list(filter(lambda x: x%2==0, a)))

momentum = lambda mass,velocity: mass*velocity
mass = float(input())
velocity = float(input())
result = momentum(mass,velocity)
print(f"{result:.2f}") 

mul = lambda x,y: x*y
x = int(input())
y = int(input()) 
result = mul(x,y)
print(f"{result:.2f}") 

force = lambda mass,acc: mass*acc
mass = float(input())
acc = float(input())
result = force(mass,acc)
print(f"{result:.2f}") 

alph = lambda alph:chr(ord(alph)-1)
print(alph(input()))       

def test1():
    a = 50 
    b = 60
    print(a,b)
def test2():
    a = 70
    b = 80
    print(a,b)
test1()
test2()

globvar = input()
def test1():
    return globvar
def test2():
    global globvar
    globvar = "Good Morning"
    return globvar
print(globvar)
test1()
test2()
print(globvar) 

a = int(input())
def changeglobal():
    global a
    a = 200
def changelocal():
    a = 500
    print(a) 
print

def test1():
    a = 50
    b = 80 
    print(a,b)
def test2():
    a = 22
    b = 44
    print(a,b) 
test1()
test2() 

x = int(input())
def test1():
    return x 
def test2():
    global x 
    x = "Good morning"
    return x 
print(x) 
test1()
test2()
print(x) 

def square(x):
    return x*x
def double(x):
    return x*2
num = int(input())
print(square(double(num))) 

def add_two(x):
    return x+2
def square(x):
    return x*x
num = int(input("Enter a number: ")) 
print(square(add_two(num)))  

num = int(input("x: "))
def square(x):
    return x*x
def increment(x):
    return x+1
def half(x):
    return x/2
print(half(increment(square(num))))
print(increment(square(num)))

x = 20
def mul():
    y = int(input("y:"))
    print(y)
    print(x)
    print("x*y: ", x*y) 
mul() 

s = 10
def call():
    p = int(input()) 
    result = (s+p)**p
    print(s)
    print(p)
    print(result) 
call()

def high_index(s):
    count = 0
    for char in s:
        count += 1
    return count-1
def reverse(s):
    reverse_s=""
    for char in s:
        reverse_s = char+reverse_s
    return reverse_s
s = input()
print(high_index(s)) 
print(reverse(s)) 

def length(s):
    count = 0
    for char in s:
        count += 1
    return count 
def reverse(s):
    reverse_s = ""
    for char in s:
        reverse_s = char + reverse_s
    return reverse_s
s = input()
print(length(s))
print(reverse(s)) 

def length(s):
    count = 0
    for char in s:
        count += 1
    return count 
def reverse(s):
    reverse_s=""
    for char in s:
        reverse_s = char + reverse_s
    return reverse_s
s = input()
print(length(s))
print(reverse(s))

import math
x = int(input())
if x>180:
    print("Enter valid angle")
else:
    radians = math.radians(x)
    rounded_value = round(radians)
    print(rounded_value)

import math
x = int(input()) 
y = int(input()) 
z = int(input()) 
result = math.gcd(x,y,z)
print(result) 

import math 
a = int(input())
b = int(input())
for i in range(a,b+1):
    result = math.sin(i)
    print(f"{result:.2f}") 

import math 
x = int(input())
result = math.log2(x)
print(f"{result:.3f}") 

import math
x = float(input()) 
result = math.log2(x)
print(f"{result:.3f}") 

import math 
x = int(input())
y = int(input())
z = int(input()) 
result = math.sqrt(x**2+y**2+z**2)
print(f"{result:.2f}") 

import math 
print("pi\t", math.pi, "\t", type(math.pi))
print("e\t", math.e, "\t", type(math.e)) 

import math
side1 = float(input()) 
side2 = float(input())
sq1 = math.pow(side1,2)
sq2 = math.pow(side2,2)
sum1 = sum([sq1,sq2])
result = math.sqrt(sum1) 
cube = math.pow(result,3)
print(f"{cube:.3f}") 

import math
x = float(input()) 
y = float(input()) 
result = math.sqrt(x**2+y**2)
print(f"{result:.3f}")

# Perfect number = a no. for which sum of its divisors (excluding itself) is equal to the number itself 
def is_perfect(number):
    if number <= 1:
        return False
    else:
        sum_of_divisors = 0
        for i in range(1, number): 
            if number%i==0:
                sum_of_divisors+=i
        return sum_of_divisors == number 
roll_number = int(input()) 
if is_perfect(roll_number):
    print("Perfect Number")
else:
    print("Not a perfect number") 

def order_chocolate(n,m):
    if m <= 0:
        return "invalid"
    else:
        remainder = n % m
        if remainder == 0:
            return 0
        else:
            return m - remainder
n = int(input()) 
m = int(input()) 
print(order_chocolate(n,m))

def geometric_sum(n):
    if n == 0:
        return 0
    else:
        return geometric_sum(n-1) + (1.0/(n**2))      
a = int(input())                                                     
if a <= 0:
    print("n must be greater than 0")
else:
    print(f"{geometric_sum(a):.2f}") 

x = int(input())
economy = int(input()) 
position = int(input()) 
if position <= x:
    print(economy)
else:
    vip = (position - x )*5
    result = vip+economy
    print(result)  

l = list(map(int, input().split(",")))
print(l) 
index = int(input()) 
f = index+1 
length = len(l) 
if f>=length or f<-length:  
    print("invalid index") 
else: 
    v= l[f] 
    nd = 0
    while(v>0):
        nd=nd+1
        v = v//10 
    print(nd) 


l1 = list(map(int, input().split(","))) 
l2 = list(map(int, input().split(","))) 
common = set(l1).intersection(set(l2))
l2_filtered = [item for item in l2 if item not in common]
print(l2_filtered)

# OR 

l1 = list(map(int, input().split(","))) 
l2 = list(map(int, input().split(","))) 
set1 = set(l1)
set2 = set(l2)
unique_to_l2 = set2 - set1 
print(list(unique_to_l2)) 

# MOCK TEST CBT-2 
k = int(input()) 
students_record = []
for _ in range(k):
    name, grade = input().split()
    students_record.append((name, int(grade)))
highest_grade = max(students_record, key=lambda item: item[1]) 
print(highest_grade) 

# MOCK TEST CBT-2
def calculate_interest(principle, years):
    rate = 0.05
    result = principle*rate*years 
    return result 
principle = int(input()) 
years = int(input()) 
interest = calculate_interest(principle, years) 
print(f"{interest:.2f}")  

def is_perfect(number):
    sum_of_divisors = 0
    for i in range(1, number):
        if number%i==0:
            sum_of_divisors+=i
    return sum_of_divisors==number
roll = int(input()) 
if is_perfect(roll):
    print("Perfect")  # 496, 6, 28, 8128 etc.....
else:
    print("Not Perfect") 

def even_ind(str1):
    return str1[::2]
print(even_ind(input()))

def odd_ind(str1):
    return str1[1::2]
print(odd_ind(input())) 

# used to print the total no. of index of the input 
s = input("str: ")
l = len(s) 
print(l-1) 

# used to print the reverse order of the input 
p = input("str: ")
print(p[::-1]) 

number_str = input("Enter a number: ")
sum_of_digits = 0
for i in number_str:
    sum_of_digits+=int(i)
print(sum_of_digits) 

original_price = float(input())
is_value = input() 
discount = original_price*0.1
if original_price>=1000 and is_value=="True":
    price = original_price-discount  
else:
    price = original_price
print(f"{price:.1f}")   
 
class Student:
    name = "Aman" 
    grade = "A+" 
s1 = Student() 
print(s1.name) 
print(s1.grade) 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 
s1 = Student("karan =" ,  90)
s2 = Student("Aman =",  94) 
print(s1.name , s1.marks) 
print(s2.name , s2.marks)   

class Student:
    college_name = "ABC College" 
    name = "Aman"  # class attribute 
    def __init__(self, name, marks):
        self.name = name  # object attribute 
        self.marks = marks 
s1 = Student("Karan", 91) 
print(s1.name) 
print(Student.name) 
# Priority of object attribute is always greater than that of class attribute 

# Methods in OOPS 
# class is a combination of attributes and methods 
class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 
    def welcome(self):
        print("welcome student,", self.name) 
    def congrats(self):
        print("Congrats you have got", self.marks , "marks")  
name = input("Enter name: ") 
marks = int(input("Enter marks: ")) 
s1 = Student("Karan" , 99) 
s1.welcome() 
s1.congrats() 

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 
    def getavg(self):
        sum = 0 
        for val in self.marks:
            sum += val 
        print("Hi", self.name, "your avg score is:", sum/3)

s1 = Student("Aman", [99, 98, 97]) 
s1.getavg() 

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True 
        self.acc = True 
        print("car started") 
car1 = car()
car1.start() 

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance 
        self.acc_no = acc_no 
    def debit(self, amount):
        self.balance-=amount
        print("Rs:", self.balance, "left") 
    def credit(self, amount):
        self.balance+=amount 
        print("Rs:", self.balance, "left") 
    def get_balance(self):
        return self.balance 
acc1 = Account(10000, 12345)
acc1.debit(2000)
acc1.credit(500) 


# Some Error is there with the below code
class TicketPricer:
    base_price = 180
    senior_discount = 0.65
    def __init__(self, age, timing):
        self.age  = age 
        self.timing = timing 
        self.price = self.calculate_age_adjusted_price() 
    def calculate_age_adjusted_price(self):
        if self.age>=60:
            return self.base_price*self.senior_discount
        else:
            return self.base_price
    def get_final_price(self):
        if self.timing == "Evening":
            final_price = self.age_price + 75 
        else:
            final_price = self.age_price
        return round(final_price, 2) 
age = int(input()) 
timing = "Evening" 
ticket = TicketPricer(age, timing)
final_price = ticket.get_final_price()
print(final_price) 



 
f = open("d:\\file.txt", "r")
x = f.read() 
print(x, type(x)) 
f.close()  


class TransferAnalyzer:
    data_weight = 5 
    speed_advantage = 1.6 
    packet_loss_cost = 14 
    def __init__(self, packet_sizes, latency_threshold, actual_latency, packet_losses):
        self.packet_sizes = packet_sizes
        self.latency_threshold = latency_threshold
        self.actual_latency = actual_latency
        self.packet_losses = packet_losses
    def compute_transfer_score(self):
        total_data = sum(self.packet_sizes) 
        transfer_score = total_data*self.data_weight 
        if self.actual_latency < self.latency_threshold:
            transfer_score *= self.speed_advantage 
            return transfer_score 
    def get_quality_score(self):
        transfer_score = self.compute_transfer_score() 
        quality_score = transfer_score - (self.packet_losses*self.packet_loss_cost)
        return round(quality_score, 2)  


class InvoiceSystem:
    TAX_RATE = 0.10
    WRAP_FEE = 5
    def __init__(self):
        self.total_bill = 0
    def scan_items(self, item_list):
        for item_name, item_price in item_list:
            cost = item_price*(1+self.TAX_RATE) 
            if item_name=="Gift":
                cost+=self.WRAP_FEE 
            self.total_bill+=cost 
    def get_total_bill(self):
        return int(self.total_bill) 


class Author:
    def __init__(self):
        self.fullName = "" 
    def inputfullName(self):
        self.fullName = input() 
    def displayfullName(self):
        return  self.fullName 
class BookAuthor(Author):
    def __init__(self):
        super().__init__() 
        self.publishedBooks = 0
    def inputBooks(self):
        self.publishedBooks = int(input()) 
    def displayBooks(self):
        return self.publishedBooks
    def generatePenName(self):
        names = self.fullName.split() 
        firstName = names[0] 
        lastName = names[1] 
        penName = firstName[:3] + lastName[-3:] 
        return penName 
    
class Plant:
    def __init__(self, name, height, water_needed):
        self.name = "" 
        self.height = 0.0 
        self.water_needed = 0.0 
    def inputPlantDetails(self):
        self.name = input() 
        self.height = float(input()) 
        self.water_needed = float(input()) 
    def displayPlantInfo(self):
        print(self.name) 
        print(f"{self.height} cm") 
        print(f"{self.water_needed }liters")  
    def TallPlant(self):
        if self.height > 50:
            return "True" 
        else:
            return "False"


class Vehicle:
    def __init__(self):
        self.make = ""
        self.model = "" 
        self.year = 0
        self.mileage = 0.0
    def input_details(self):
        self.make = input() 
        self.model = input() 
        self.year = int(input()) 
        self.mileage = float(input()) 
class CarInfo(Vehicle):
    def __init__(self):
        super().__init__() 
        self.is_electric = False 
    def input_car_info(self):
        super().input_details() 


def glow(beads):
    if not beads:
        return 0
    print(beads[-1], end=' ')
    return 1+glow(beads[:-1])
print(glow(["red", "blue", "green"])) 

def clap(word):
    if len(word) <= 1:
        return word 
    return word[0] + clap(word[2:])
print(clap("lamplight")) 
    

x = input() 
print(x[0]+x[0]+x) 

# 1. Print the numbers from 21 to 40 

for i in range(21,41):
    print(i) 

# 21 to 60 divisible by 3 and 5 

for i in range(21, 61):
    if i % 3 == 0 and i % 5 == 0:
        print(i) 



n = int(input())
for i in range(1, n):
    if i%2==0:
        print(i) 

# find the sum of even numbers from 21 to 40 

sum = 0
for i in range(21, 41):
    if i % 2==0:
        sum+=i
        print(i) 

# print the prime numbers from the list 
input_list = list(input())

# count the total number of vowels from your name 

words = "Ansh Aggarwal"
vowels = "aeiouAEIOU"
count = 0
for letter in words:
    if letter in vowels:
        count += 1
print(count)  

# print your name without vowels 
words = "Ansh Aggarwal"
vowels = "aeiouAEIOU"
count = 0
for letter in words:
    if letter not in vowels: 
        count += 1
print(count)  

# count of total number of spaces from the string 
string = str(input()) 

# count of total letters from the string 

m = input() 
print(len(m)) 

# find the sum of even digits of your number 

N = input() 
sum = 0
for i in range(1,N):
    if i%2==0:
        sum+=i
        print(sum) 



# print the list of prime digits of your number 


for i in range(20,41):
    print(i)

a=[x for x in range(21,61) if x%3==0 and x%5==0]
print(a)

# check the number is a palindome
a=input()
if a==a[::-1]:
    print("palindrome")
else:
    print("not a palindrome")


# check the number is a armstrong number
a=input("Enter a number: ")
b=0
for i in a:
    b+=int(i)**3
if int(a)==b:
    print("armstrong")
else:
    print("not a armstrong")


# check the number is even or odd
a=int(input("Enter a number: "))
if a%2==0:
    print("Even")
else:
    print("Odd")


# find the sum of even from 21,40
a=0
for i in range(21,41):
    if i%2==0:
        a+=i
print(a)


# print prime number from a list
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in a:
    if i > 1:
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)




# count the total number of vowals from your name
a="karanjeet singh"
b=0
for i in a:
    if i in "AEIOUaeiou":
        b+=1
print(b)


# print your name without vowels
a="Karanjeet Singh"
b=""
for i in a:
    if i not in "AEIOUaeiou":
        b+=i
print(b)


# count the total number of space from the string
a="Hello, I study in 425TR"
b=0
for i in a:
    if i.isspace():
        b+=1
print(b)


# count the total number of letters from the string
a="Hello, I study in 425TR"
b=0
for i in a:
    if i.isalpha():
        b+=1
print(b)



# find the sum of even digit of a number
a=input("Enter a number: ")
b=0
for i in a:
    if int(i)%2==0:
        b+=int(i)
print(b)


# print the list of prime digit of a number
a = input("Enter a number: ")
b = []
for j in a:
    if int(j) in [2, 3, 5, 7]:
        b.append(int(j))
print(b)


# print the list of prime digit of a number
# find the sum of even digit of a number
# count the total number of space from the string
# count the total number of letters from the string
# count the total number of vowals from your name
# print your name without vowels
# print prime number from a list
# find the sum of even from 21,40
# check the number is even or odd
# check the number is a palindome
# check the number is a armstrong number










































































































































































































































































































































































































































































































































































































































































