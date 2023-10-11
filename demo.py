#variables
#numbers

#define an integer
myint = 7
print(myint)

#define a floating point number
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes" #"" makes it easy to include apostrophes
print(mystring)

#simple operators
one=1
two=2
three=one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a = 10
b = 20
print(b-a)

a = 2
b = 3
if a < b :
    result =  "True"
else: result =   "False"
print(result)

dividend = 50
divisor = 4
remainder = dividend % divisor
print(remainder)

#multiple variables
a, b = 3, 4
print(a,b)

#list
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # print 1
print(mylist[1]) # print 2
print(mylist[2]) # print 3

#prints out 1,2,3
for x in mylist:
    print(x)

my_list = [1, "apple", 3.14]
my_list.append("banana")
print(my_list)

#arithmetic operators
number = 1+2*3/4.0
print(number)

#modulo(%) operator
remainder = 11%3
print(remainder)

#using two multiplication symbols makes a power relation
squared = 7**2
cubed = 2**3
print(squared)
print(cubed)

#using operators with list
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

a = 14
b = 'my name is Mr. superStar'
print(type(a))
print(type(b))

def greet(name):
    print(f"Hello, {name}!")
greet("Arvind")

#Data type tuple
testtuple = (25, 78, 98, 0.90)
print(testtuple)
print(len(testtuple))
print(type(testtuple))

#sets
testset = {40, 60, 20, 50, 40, 40}
print(testset)
print(len(testset))
print(type(testset))

#testDisc
testDisc = {"first":40,"second":60,"third": 20, "a":50}
print(testDisc)
print(len(testDisc))
print(type(testDisc))

#using python list
testlist = [50,100,"arvind","greeting",65,255]
print(testlist)
print(testlist[3])
#adding to python list
testlist.append ("hello") # for adding at back of the list
testlist.insert (3, "pandit") # for adding in-between the list
print(testlist)
#update list
testlist[0] = "first" # 0 indicates list squence in python
print(testlist)
#python print opr
print(len(testlist))
print(testlist[-2])
print(testlist[1:3])
print(testlist.index("pandit"))
#checking value in list
val = ("arvind" in testlist)
print (val)
val = testlist.pop(3) #pops up the value in list
print(val)
#delete list
#del testlist
#testlist.clear() # removes the values in the list
#sorting list
#testlist.sort()
#testlist.reverse() #reverse the list

#input function
#checking number validation
val = input("Enter a number 1-9:")
val = val.strip() ## Remove leading and trailing spaces from the input

if val.isnumeric():
    num = int(val)
    if 1 <= num <= 9:
        message = "You entered " + val
    else:
        message = "Please enter a number between 1 and 9."
else:
    message = "Sorry, try again."

print(message)

#checking names
user_input = input("What is your name?")
user_input = user_input.strip() ## Remove leading and trailing spaces from the input

if user_input.isalpha():
    print("You entered:", user_input)
else:
    print("Sorry, try again!")

print(user_input)

#checking ID number
while True:
    member_id = input("Enter ID: ")
    member_id = member_id.strip()

    if member_id.isnumeric():
        if member_id.startswith("0"):
            print("Authorized:", member_id)
            break  # Exit the loop if authorized
        else:
            print("Unauthorized:", member_id)
            break  # Exit the loop if unauthorized
    else:
        print("Invalid input. Please enter a numeric ID.")
 

#checking driver id and name
# Predefined driver names and IDs
driver_names = ["john", "smith", "tina", "jakey", "jamson"]
driver_ids = [101, 203, 503, 505, 105]

while True:
    driver_name = input("Enter driver name: ").strip()
    driver_id_str = input("Enter driver ID: ").strip()

    if not driver_id_str.isnumeric():
        print("Invalid input. Driver ID must be numeric.")
        continue

    driver_id = int(driver_id_str)

    if driver_name in driver_names and driver_id in driver_ids:
        print("Authorized person:", driver_name, driver_id)
        break
    else:
        print("Not authorized:", driver_name, driver_id)
        break

# Defining a dictionary to store the mappings between driver names and IDs
driver_data = {
    "john": 101,
    "smith": 203,
    "tina": 503,
    "jakey": 505,
    "jamson": 105
}

while True:
    driver_name = input("Enter driver name: ").strip().lower()  # Convert to lowercase for case-insensitive matching

    # Check if the entered name is in the dictionary
    if driver_name in driver_data:
        driver_id = driver_data[driver_name]
        print("Authorized person:", driver_name, driver_id)
        break
    else:
        print("Not authorized:", driver_name)
        break

#mini calculator with int
num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))
total = num1 - num2 #replace the sign with any {+, -, *, /} for calculation
print("total output", total)
#mini calculator with float
num1 = float(input("First Number:"))
num2 = float(input("Second Number:"))
total = num1 - num2 #replace the sign with any {+, -, *, /} for calculation
print("total output", total)

#mini project #code bouncer allowed in or not
age_input = input("Enter your age: ").strip()
if age_input.isnumeric():
    age = int(age_input)#converts age into integer
    if age >= 21:
        print ("Great you are eligible to drink 😍")
    elif age >= 19:
        print("Not legally eligible for dringking! You may enjoy Soft drink 😊")
    else:
        print("Not a legal age for drinking 😑")

#simple lambda
value = lambda a, b : a + b
output = value(10,20)
print(output)

print(value(5,6))















 