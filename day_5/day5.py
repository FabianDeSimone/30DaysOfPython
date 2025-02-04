# Exercises level 1:

# Declare an empty list

list = list()
list2 = []
print(list)
print(list2)

# Declare a list with more than 5 items

list3 = ['a', 'b', 'c', 'd', 'e', 'f']

# Find the length of your list

print(len(list3))

# Get the first item, the middle item and the last item of the list

first = list3[0]
middle = list3[len(list3)//2]
last = list3[-1]
print(first)
print(middle)
print(last)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

name = 'Fabián De Simone'
age = 28
height = 1.70
marital_status = 'single'
address = 'San Martin 1440'
mixed_data_types = [name, age, height, marital_status, address]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()

print(it_companies)

# Print the number of companies in the list

print(len(it_companies))

# Print the first, middle and last company

first = it_companies[0]
middle = it_companies[len(it_companies)//2]
last = it_companies[-1]

print(first)
print(middle)
print(last)

# Print the list after modifying one of the companies

it_companies[0] = 'Twitter'
print(it_companies)

# Add an IT company to it_companies

it_companies.append('Samsung')

# Insert an IT company in the middle of the companies list

it_companies.insert(len(it_companies)//2, 'Sony')

# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[3] = it_companies[3].upper()

# Join the it_companies with a string '#; '.

print('#; '.join(it_companies))

# Check if a certain company exists in the it_companies list.

print('Apple' in it_companies)

# Sort the list using sort() method

it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method

it_companies.reverse()

# Slice out the first 3 companies from the list

print(it_companies[:3])

# Slice out the last 3 companies from the list

print(it_companies[-3:])

# Slice out the middle IT company or companies from the list

print(it_companies[len(it_companies)//2])

# Remove the first IT company from the list
print(it_companies)
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list

it_companies.pop(len(it_companies)//2)
print(it_companies)

# Remove the last IT company from the list

it_companies.pop(-1)

# Remove all IT companies from the list

it_companies.clear()

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack = front_end.copy()
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Redux')+2, 'SQL')

# Exercises: Level 2

# The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort()
print(ages[0])
print(ages[-1])

# Add the min age and the max age again to the list

ages.append(ages[0])
ages.append(ages[-1])

# Find the median age (one middle item or two middle items divided by two)

middle = len(ages)//2

if len(ages) % 2 == 0:
    median = (ages[middle] + ages[middle-1]) / 2
else:
    median = ages[middle]

print(median)

# Find the average age (sum of all items divided by their number)

average = sum(ages) / len(ages)

# Find the range of the ages (max minus min)

range = ages[-1] - ages[0]

# Compare the value of (min - average) and (max - average), use abs() method

print(abs(ages[0] - average))

print(abs(ages[-1] - average))

# Find the middle country(ies) in the countries list

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(countries[len(countries)//2])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

if(len(countries) % 2 == 0):
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else: 
    first_half = countries[:len(countries)//2+1]
    second_half = countries[len(countries)//2+1:]

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *scandic = countries

