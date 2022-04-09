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
 print('One of thetop 5 baseball players, ever!')
# (c)
