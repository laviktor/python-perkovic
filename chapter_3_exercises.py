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
