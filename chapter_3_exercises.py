# 3.16
eval('2 * 3 + 1')
eval('hello')
eval("'hello’ + ' '+ 'world!'")
eval("'ASCII'.count('I')")
eval('x = 5')
# errors results in the second, third, and last code. There was nothing to evaluate as a Python expression
# 3.17
a, b, c = 3, 4, 5
if a < b:
  print('OK')
if c < b:
  print('OK')
if a + b == c:
  print('OK')
if a**2 + b**2 == c**2:
  print('OK')
# 3.18
if a < b:
  print('OK')
if c < b:
  print('NOT OK')
if a + b == c:
  print('NOT OK')
if a**2 + b**2 == c**2:
  print('OK')
# 3.19
lst19 = ['January', 'February', 'March']
for i in lst19:
  print(i[0]+i[1]+i[2])
# 3.20
lst20 = [2, 3, 4, 5, 6, 7, 8, 9]
for i in lst20:
  if i**2 % 8 == 0:
    print(i)
# 3.21
for i in range(0, 2):
  print(i, end=" ")
for i in range(0, 1):
  print(i, end=" ")
for i in range(3, 7):
  print(i, end=" ")
for i in range(1, 2):
  print(i, end=" ")
for i in range(0, 4, 3):
  print(i, end=" ")
for i in range(5, 22, 4):
  print(i, end=" ")
# 3.22
list22 = eval(input('Enter list of words: '))
for i in list22:
  if 'secret' != i:
    print(i)
# 3.23
list23 = eval(input('Enter list: '))
for i in list23:
  if i[0] in 'abcdefghijklmABCDEFGHIJKLM':
    print(i)
# 3.24
list24 = eval(input('Enter a list: '))
print('The first list element is', list24[0])
print('The last list element is', list24[-1])
# 3.25
int25 = eval(input('Enter n: '))
for i in range(4):
  print(int25 * i)
# 3.26
int26 = eval(input('Enter n: '))
for i in range(int26):
  print(i ** 2)
# 3.27
int27 = eval(input('Enter n: '))
for i in range(1, int27 + 1):
  if int27 % i == 0:
    print(i)
# 3.28
num28_1 = eval(input('Enter first number: '))
num28_2 = eval(input('Enter second number: '))
num28_3 = eval(input('Enter third number: '))
num28_4 = eval(input('Enter last number: '))
avg28 = (num28_1 + num28_2 + num28_3) / 3
if num28_4 == avg28:
    print('Equal')
# 3.29
x = eval(input('Enter x: '))
y = eval(input('Enter y: '))

# circle centered at origin with radius 8: x^2 + y^2 = 8^2

radius = 8

if (x**2 + y**2) <= radius ** 2:
  print('It is in!')
# 3.30
num30 = eval(input('Enter n: '))
num30_thousands = num30 // 1000
print(num30_thousands)
num30_hundreds = num30 // 100 - num30_thousands * 10
print(num30_hundreds)
num30_tens = num30 // 10 - num30_thousands * 100 - num30_hundreds * 10
print(num30_tens)
print(num30 - num30_thousands * 1000 - num30_hundreds * 100 - num30_tens * 10)
# 3.31
ex31a = 'abc'
ex31b = 'dna'
def reverse_string(x):
  print(x[-1]+x[-2]+x[-3])
reverse_string(ex31a)
reverse_string(ex31b)
# 3.32
ex32a = 10
ex32b = 10
ex32c = 10
ex32d = 35
ex32e = 10
ex32f = 45

# function in terms of returning
def pay1(x, y):
  if y <= 40:
    return x * y
  else:
    return ((x * 40) + (x * 1.5 * (y - 40)))
print(pay1(ex32a, ex32b))
print(pay1(ex32c, ex32d))
print(pay1(ex32e, ex32f))
print()
# function in terms of printing
def pay2(x, y):
  if y <= 40:
    print(x * y)
  else:
    print(((x * 40) + (x * 1.5 * (y - 40))))
pay2(ex32a, ex32b)
pay2(ex32c, ex32d)
pay2(ex32e, ex32f)
print()

# 3.33
ex33a = 1
ex33b = 2
def prob(x):
	return 2 ** -x
print(prob(ex33a))
print(prob(ex33b))
print()

# 3.34
ex34a = 123
ex34b = 908
def reverse_int(x):
	last = x // 100
	middle = (x // 10)
	first = (x - last * 100 - middle * 10)
	return first, middle, last
print(reverse_int(ex34a))
print(reverse_int(ex34b))
print()

# 3.35
