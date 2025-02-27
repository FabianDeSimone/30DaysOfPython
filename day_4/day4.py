# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print('Coding' + ' ' + 'For' + ' ' + 'All')

# Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# Print the variable company using print().

print(company)

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.

print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.index('Coding'))
print(company.find('Coding'))
print('Coding' in company)

# Replace the word coding in the string 'Coding For All' to Python.

print(company.replace('Coding', 'Python'))

# Change Python for Everyone to Python for All using the replace method or other methods.

string = 'Python for Everyone'
print(string.replace('Everyone', 'All'))

# Split the string 'Coding For All' using space as the separator (split()) .

print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

# What is the character at index 0 in the string Coding For All.

print(company[0])

# What is the last index of the string Coding For All.

print(company[-1]) # -1 is the last index

# What character is at index 10 in "Coding For All" string.

print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.

string = 'Python For Everyone'
words = string.split()
acronym = ''
for word in words:
    acronym += word[0].upper()
print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.

string = 'Coding For All'
words = string.split()
acronym = ''
for word in words:
    acronym += word[0].upper()
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All.

print(company.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.

print(company.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.

print(company.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# Use rfind to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.

print(sentence.rfind('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.

endpos = sentence.rfind('because') + len('because')
print(endpos)
print(sentence[31:endpos])

# Find the position of the first occurrence of the word 'because' in the sentence: 'You cannot end a sentence with because because because is a conjunction'.

print(sentence.find('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.

startpos = sentence.find('because')
endpos = sentence.rfind('because') + len('because')
print(sentence[startpos:endpos])

# Does ''Coding For All' start with a substring Coding?

company = "Coding For All"
print(company.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?

print(company.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

company = '   Coding For All      '
print(company.strip())

# Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python, CodingForAll, coding_for_all, and '30_days_of_python'.

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# Use the new line escape sequence to separate the following sentences. 'I am enjoying this challenge. I just wonder what is next.'

sentence = 'I am enjoying this challenge. I just wonder what is next.'
print(sentence.replace('. ', '.\n'))

# Use a tab escape sequence to write the following lines

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:

name = 'Asabeneh'
age = 250
country = 'Finland'
city = 'Helsinki'
print(f'{name} is {age} years old. He lives in {city}, {country}.')
print('{} is {} years old. He lives in {}, {}.'.format(name, age, city, country))

# Make the following using string formatting methods:

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} square meters.')