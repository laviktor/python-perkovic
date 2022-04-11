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
