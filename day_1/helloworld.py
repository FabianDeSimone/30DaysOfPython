# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(5 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

#Exercise: Level 2
#1 Check the python version you are using
#py --version
#2 Create a new file named helloworld and do the following operations. The operands are 3 and 4.
# Addition(+)
print(3 + 4)
# Subtraction(-)
print(3 - 4)
# Multiplication(*)
print(3 * 4)
# Division(/)
print(3 / 4)
# Modulus(%)
print(3 % 4)
# Exponential(**)
print(3 ** 4)
# Floor division operator(//)
print(3//4)

#3 Write strings. The strings are the following: 
# Your name
# Your family name
# Your country
# I am enjoying 30 days of python
print("Fabián")
print("De Simone")
print("Argentina")
print("I am enjoying 30 days of python")

#4 Check the data types of the following data

#10
#9.8
#3.14
#4 - 4j
#['Asabeneh', 'Python', 'Finland']
#Your name
#Your family name
#Your country

print(type(10))          # Int
print(type(9.8))         # Float
print(type(3.14))        # Float
print(type(4 - 4j))      # Complex number
print(type(['Asabeneh', 'Python', 'Finland']))   # List
print(type('Fabián'))    # String
print(type('De Simone')) # String
print(type('Argentina')) # String

#Exercise: Level 3
#Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
print(type(19))
print(type(19.0))
print(type(19 + 0j))
print(type("19"))
print(type(True))
print(type([19]))
print(type((19,)))
print(type({19}))
print(type({"Integer": 19}))
#Find an Euclidian distance between (2, 3) and (10, 8)
import math
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)
#Another way
p = (2, 3)
q = (10, 8)
distance = ((q[0] - p[0])**2 + (q[1] - p[1])**2)**0.5
print(distance)