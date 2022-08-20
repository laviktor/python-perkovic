# 4.1
s = '0123456789'
s[2:5]
s[7:9]
s[1:8]
s[0:4]
s[7:]

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
  for i in range(2, x):
    if i % 2 == 0 or i % 3 == 0:
      print(i, end = ', ')
even(ex4a)
# Test this out, because it is not working on the online compiler

# 4.5
first = 'John'
last = 'Doe'
street = 'Main Street'
number = 123
city = 'AnyCity'
state = 'AS'
zipcode = '09876'
print('{} {}'.format(first, last) + '\n' + '{} {}'.format(str(number), street) + '\n' + '{}, {} {}'.format(city, state, zipcode))

# 4.6
students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.00])
students.append(['Columbus', 'Maria', 'Senior', 2.50])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])

def roster(x):
  # Changed "Average Grade" to "GPA" for better nomenclature
  print('Last First Class GPA')
  format_str = '{0:10}{0:10}{0:10}{0:8.2}'
  for i in range(0, 5):
roster(students)

# 4.7

def stringCount(x, y):
  x = open(x, y)
