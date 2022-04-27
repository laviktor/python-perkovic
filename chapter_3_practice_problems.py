# 3.1
fah = eval(input('Enter the temperature in degrees Fahrenheit: '))
cel = (5/9)*(fah - 32)
cel_convert = 'The temperature in degrees Celsius is '
# The following code is incorrect. It tries to concatenate string and float:
# print(cel_convert + cel)
print(cel_convert, cel)
# 3.2
# (a)
age = eval(input('Enter your age: '))
if age > 62:
 print('You can get your pension benefits.')
# (b)
name = input('Enter a baseball player''s last name: ')
list2 = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
if name in list2:
 print('One of the top 5 baseball players, ever!')
# (c)
if hits > 10 and shield == 0:
 print('You are dead...')
# (d)
# if direction == 'north', ' <-- This is incorrect because they are string, despite having an if statement of true/false
# 3.3
# (a)
if year % 4 == 0:
 print('Could be a leap year.')
else:
 print('Definitely not a leap year.')
# (b)
if ticket == lottery:
 print('You won!')
else:
 print('Better luck next time...')
# 3.4
id = ['joe', 'sue', 'hani', 'sophie']
user = input('Login: ')
if user in id:
	print('You are in!')
else:
	print('User unknown.')
print('Done.')
# 3.5
l = input('Enter word list: ')
for x in l:
	if len(x) == 4:
		print(x)
# This print out bypasses the printed dummy variable cycling through the for loop...why?
# Even though the input() is suppose to be a string object, we still have to pass through eval()...why?
# It appears that if literally ANY other object string, input() has to be passed through eval()
# 3.6
for i in range(10):
	print(i)
for i in range(2):
	print(i)
# 3.7
for i in range(3, 13):
	print(i)
for i in range(0, 9, 2):
	print(i)
for i in range(0, 24, 3):
	print(i)
for i in range(3, 12, 5):
	print(i)
# 3.8
def a(x, y):
	return (x + y)/2
# 3.9
import math
r = eval(input('Enter a radius: '))
def circumfrence(r):
	return 2*math.pi*r
print(circumfrence(r))
# 3.10
def negatives(x):
	for i in x:
		if i < 0:
			print(i)
# 3.11
def average(x, y):
	'returns average of x and y'
	returns (x + y)/2
# 3.12 - hand-written work
# 3.13
team = ['Ava', 'Eleanor', 'Clare', 'Sarah']
team[0], team[-1] = team[-1], team[0]
# 3.14
ingredients = ['flour', 'sugar', 'butter', 'apples']
def swapFL(lst):
	lst[0], lst[-1] = lst[-1], lst[0]
