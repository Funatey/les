'''

products = ['яблоко', 'груша', 'арбуз', 'банан', 'мандарин']
print (products)

a = int(input('выберите индекс товара от 0-4: '))
b = products.pop(a) 
print (b)
print (products)
	if a > 4 and a < 0:
		print ('Danger')



points = 0
print ('ваши баллы: ', points)
a = '1)1+5=, 2)8+2=, 3)6+3=: '
print (a)
b  = int(input('gde budet 10: '))
if b == 2:
	point = points + 1
	print ('правильно! ваши баллы теперь:', point )

else:
	print ('nepravilno')



points = 0

print ('ваши баллы: ', points)
a = '1) 1+1=: '
print (a)
b  = int(input('write answer: '))
c = '2) 2+2=: '
print (c)
d = int(input('write answer: '))
e = '3) 3+3=: '
print (e)
f = int(input('write answer: '))
if b == 2:
	points += 1
	print ('1)good')
else:
	print ('1) is bad')
	print ('total points: ', points)
if d == 4:
	points +=1
	print ('2)great')
else:
	print ('2) is bad')
	print ('total points: ', points)
if f == 6:
	points +=1
	print ('3)perfect')
	print ('test proiden')
	print ('total points: ', points)
else:
	print ('3) is bad')
	print ('total points: ', points)

'''

a = ['a','b','c','d','e','f','g','www','eqw','pep']
b = int(input('write number 0-9: '))
print (a[b:])










