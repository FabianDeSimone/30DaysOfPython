# Exercises - Day 3


# Declare your age as integer variable

age = 28

# Declare your height as a float variable

height = 1.70

# Declare a variable that store a complex number

complex_number = 1 + 3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is: ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print("The perimeter of the triangle is: ", a + b + c)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter = 2*(length + width)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = int(input("Enter radius: "))
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius

# Calculate the slope, x-intercept and y-intercept of y = 2x -2

slope1 = 2
x_intercept = (0,-2)
y_intercept = (-1,0)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = (y2 - y1)/(x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#Compare the slopes in tasks 8 and 9.

print(slope1 == slope2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x1 = int(input("Enter x: "))
y = x1**2 + 6*x1 + 9
print("y is: ", y)
x2 = int(input("Enter x: "))
y = x2**2 + 6*x2 + 9
print("y is: ", y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len('python') is not len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'  

print('on' in 'python' and 'on' in 'dragon')

#  hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print('jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python

print('on' not in 'python' and 'on' not in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string

str(float(len('python')))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

number = int(input("Enter a number: "))
print(number % 2 == 0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

print(7//3 == int(2.7))

# Check if type of '10' is equal to type of 10

print(type('10') == type(10))