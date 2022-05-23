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
