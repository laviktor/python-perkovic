#Practice Problem 2.1
#Write Python algebraic expresions corresponding to the following statements:
#(a) The sum of the first 5 positive integers
1+2+3+4+5
#(b) The average of Sara (age 23), Mark (age 19), and Fatima (age 31)
(23+19+31)/3
#(c) The number of times 73 goes into 403
403//73
#(d) The reaminder when 403 is divided by 73
403%73
#(e) 2 to the 10th power
2**10
#(f) The absolute value of the difference between Sara's highet (54 inches) and Mark's height (57 inches)
abs(54-57)
#(g) The lowest price among the following prices: $34.99, $29.95, and $31.50
min(34.99, 29.95, 31.50)
#Practice Problem 2.2
#Translate the following statements into Python Boolean expressions and evaluate them:
#(a) The sum of 2 and 2 is less than 4.
2+2<4
#(b) The value of 7 // 3 is equal to 1 + 1.
7//3==1+1
#(c) The sum of 3 squared and 4 squared is equal to 25.
3**2+4**2==25
#(d) The sum of 2, 4, and 6 is greather than 12.
2+4+6>12
#(e) 1,387 is divisible by 19.
1387%19==0
#(f) 31 is even.
31%2==0
$(g) The lowest price among $34.99, $29.95, and $31.50 is less than $30.00
min(34.99, 29.95, 31.50)<30.00
#Practice Problem 2.3
#Write Python statements that correspond to the below actions and execute them:
#(a) Assign integer 3 to variable a.
a=3
#(b) Assign 4 to variable b.
b=4
#(c) Assign to variable c the value of expression a * a + b * b
c=a*a+b*b
#Practice Problem 2.4
#Start by executing the assignment statements:
s1='ant'
s2='bat'
s3='cod'
#Write Python expressions using s1, s2, and s3 and operators + and * that vaulate to:
#(a) 'ant bat cod'
s1+' '+s2+' '+s3
#(b) 'ant ant ant ant ant ant ant ant ant ant '
(s1+' ')*10
#(c) 'ant bat bat cod cod cod'
s1+(' '+s2)*2+(' '+s3)*3
#(d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
(s1+' '+s2+' ')*7
#(e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '
(s2*2+s3+' ')*5
#Practice Problem 2.5
#Start by executing the assignment:
s='0123456789'
#Now write expressions using string s and the indexing operator that evulate to:
#(a) '0'
s[0]
#(b) '1'
s[2]
#(c) '6'
s[6]
#(d) '8'
s[8]
#(e) '9'
s[9]
#Practice Problem 2.6
#First execute the assignment
words=['bat','ball','barn','basket','badminton']
#Now write two Python expressions that evulate to the first and last, respectively, word in words, in dictionary order.
min(words)+', '+max(words)
#Practice Problem 2.7
#Given the list of student homework grades
grades=[9,7,7,10,3,9,6,6,2]
#Write:
#(a) An expression that evaluates to the number of 7 grades
grades.count(7)
#(b) A statement that changes the last grade to 4
grades[9]=4 #Better syntax is to start from the negative portion
#(c) An expression that evulates to the maximum grade
max(grades)
#(d) A statement that sorts the list grades
grades.sort()
#(e) An expression that evulates to the average grade
sum(grades)/len(grades)
#Practice Problem 2.10
#Write Python expressions corresponding to the following:
#(a) The length of the hypotenuse in a right triangle whose other two sides have lengths a and b
math.sqrt(a**2+b**2)
#(b) The value of the expression that evulatess whether the lenth of the above hyptoenuse is 5
math.sqrt(a**2+b**2)==5
#(c) The area of a disk of radius a
math.pi*a**2
#(d) The value of the Boolean expression that checks whether a point with coordinates x and y is inside a circle with center (a,b) and radius r
(x-a)**2+(y-b)**2<r**2
