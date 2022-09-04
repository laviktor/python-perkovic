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
  title_format = '{0:10}{1:10}{2:10}{3:10}'
  # Changed "Average Grade" to "GPA" for better nomenclature
  # Spacing was incorrect, thus "Average Grade" shall be reverted
  print(title_format.format('Last', 'First', 'Class', 'Average Grade'))
  table_format = '{0:10}{1:10}{2:10}{3:8.2f}'
  for i in range(0, len(students)):
    print(table_format.format(students[i][0], students[i][1], students[i][2], students[i][3]))
roster(students)

# 4.7

# To count text from a file, suppose the file is assigned as x, then
# x.read().count(' ')
# where x.read() is the text as a string, assigned x
# the .count() is a string function counting the desired string

def stringCount(file_name, target):
  in_file = open(file_name, 'r')
  occurrences = in_file.read().count(target)
  
  return occurrences

# 4.8
def words(file_name):
    in_file = open(file_name, 'r')
    content = in_file.read()
    in_file.close()
    
    word_list = content.split()
    print(word_list)
    # Has to omit the punctuations as well
    
# 4.9
def myGrep(x, y):
  
# 4.10
# Explain what causes the syntax error in each statement just listed. Then write a correct version of each Python statement.
if x == 5
# SyntaxError: invalid syntax
# Correction - colon is needed after conditional phase
if x == 5:
print 'hello'
# SyntaxError: Invalid syntax
# Correction - parenthesis was omitted
print('hello)
lst = [4;5;6]
# SyntaxError: Invalid syntax
# Correction - Commas used, not semicolons
lst = [4,5,6]
for i in range(10):
print(i)
# SyntaxError: expected an indented block
# Correction - Indent is needed for any print statements within the loop
for i in range(10):
      print(i)

# 4.11
import time
t = time.localtime(1500000000)

def strftime():
      format
