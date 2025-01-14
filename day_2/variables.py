#Day 2: 30 Days of python programming'

#Exercises: Level 1
#Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
#Write a python comment saying 'Day 2: 30 Days of python programming'
#Declare a first name variable and assign a value to it
#Declare a last name variable and assign a value to it
#Declare a full name variable and assign a value to it
#Declare a country variable and assign a value to it
#Declare a city variable and assign a value to it
#Declare an age variable and assign a value to it
#Declare a year variable and assign a value to it
#Declare a variable is_married and assign a value to it
#Declare a variable is_true and assign a value to it
#Declare a variable is_light_on and assign a value to it
#Declare multiple variable on one line

firstName = "Fabián"
lastName = "De Simone"
fullName = firstName + " " + lastName
country = "Argentina"
year = 2025
is_married = False
is_true = True
is_light_on = True
a, b , c = 10, 20, 30

#Exercises: Level 2



#Check the data type of all your variables using type() built-in function

print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))

#Using the len() built-in function, find the length of your first name

print(len(firstName))

#Compare the length of your first name and your last name

print(len(firstName) == len(lastName))

#Declare 5 as num_one and 4 as num_two

num_one, num_two = 5, 4

#Add num_one and num_two and assign the value to a variable total

total = num_one + num_two

#Subtract num_two from num_one and assign the value to a variable diff

diff = num_one - num_two

#Multiply num_two and num_one and assign the value to a variable product

product = num_two * num_one

#Divide num_one by num_two and assign the value to a variable division

division = num_one / num_two

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

remainder = num_two % num_one

#Calculate num_one to the power of num_two and assign the value to a variable exp

exp = num_one ** num_two

#Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num_one // num_two

#The radius of a circle is 30 meters.

radius = 30

#Calculate the area of a circle and assign the value to a variable name of area_of_circle

area_of_circle = 3.14 * radius ** 2

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

circum_of_circle = 2 * 3.14 * radius

#Take radius as user input and calculate the area.

radius = int(input("Enter the radius: "))

print(radius)

area_of_circle = 3.14 * radius ** 2

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

print(help('keywords'))
