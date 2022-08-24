# 4.1
s = '0123456789'
s[2:5]
s[7:9]
s[1:8]
s[0:4]
s[7:10]

# 4.2
forecast = 'It will be a sunny day today'
count = forecast.count('day')
count
weather = forecast.find('sunny')
weather
change = forecast.replace('sunny', 'cloudy')
change

# 4.3
last = 'Smith'
first = 'John'
middle = 'Paul'
print(last, first, middle, sep = '\t')

# 4.4
ex4a = 17
def even(x):
  for i in range(1, x + 1):
    if i % 2 == 0 or i % 3 == 0:
      print(i, end = ', ')
even(ex4a)
# Edits made and worked on Python3 on macOS

# 4.5
first = 'John'
last = 'Doe'
street = 'Main Street'
number = 123
city = 'AnyCity'
state = 'AS'
zipcode = '09876'
print('{} {}'.format(first, last) + '\n' + '{} {}'.format(str(number), street) + '\n' + '{}, {} {}'.format(city, state, zipcode))
# Alternatively
print('\n{} {}\n{} {}\n{}, {} {}\n'.format(first, last, number, street, city, state, zipcode))

# 4.6
students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.00])
students.append(['Columbus', 'Maria', 'Senior', 2.50])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])

def roster(x):
  title_format = '{0:10}{0:10}{0:10}{0:10}'
  # Changed "Average Grade" to "GPA" for better nomenclature
  print(title_format.format('Last', 'First', 'Class', 'GPA'))
  table_format = '{0:10}{0:10}{0:10}{0:8.3}'
  for i in range(0, len(students)):
roster(students)

# 4.7

def stringCount(filename, target):
  infile = open(filename, 'r')
  content = infile.read()
  infile.close()
  
  return filename.count(target)

# To count text from a file, suppose the file is assigned as x, then
x.read().count(' ')
# where x.read() is the text as a string, assigned x
# the .count() is a string function counting the desired string
