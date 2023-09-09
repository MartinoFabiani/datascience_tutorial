#integers
x=2
y=10

#floating-point numbers
pi=3.14159


#string
name= "John Doe"

#boolean
is_python_fun = True

#arithmetic operations
result= x+y
product= x*y
quotient = x/y

#string concatenation
full_name= name + "Smith"

#comparison
is_equal= x==y
is_greater= x>y

#If-else statement
if x>y:
    print("x is greater than y")
elif x<y:
    print("x is less than y")
else:
    print("x is equal to y")

#For loop
for i in range(5):
    print(i)

#While loop
count=0
while count<5:
    print(count)
    count += 1

#Lists (ordered, changeable)
fruits =["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0])  #accessing elements

#Dictionaries (key-value pairs)
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"]) #accessing values by key

#FUNCTION
def greet(name):
    return "Hello, " + name + "!"

message = greet("Alice")
print(message)

#Libraries
pip install numpy pandas matplotlib

import numpy as np

data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
print(mean)



