'''
list1 = []
a = input('add word: ')
b = input('2add word: ')
c = input('3add word: ') 
list1.append(a)
list1.append(b)
list1.append(c)
print(list1)
if (len(a + b + c) > 20):
	if a.isalpha() and b.isalpha() and c.isalpha():
		if len(a) > len(b) and len(a) > len(c):
			list1.remove(a)
			print(' '.join(list1).upper())
		elif len(b) > len(a) and len(b) > len(c):
			list1.remove(b)
			print(' '.join(list1).upper())
		elif len(c) > len(a) and len(c) > len(b):
			list1.remove(c)
			print(' '.join(list1).upper())
	else:
		print('please only words')
else:
	print('please > 20')



a = input('add your @gmail: ')
if a.endswith('@gmail.com') or a.endswith('@mail.ru'):
	print('your code:123456')
	b = int(input('enter code: '))
	c = 123456
	if c == b:
		print('succes')
	else:
		print('eror code')
else:
	print('eror')


a = 2897607
if  a % 3 == 0:
	d = 2897607 / 3
	e = d * d 
	print(len(str(e)))
	if len(str(e)) > 10:
		f = str(e).replace('3', '0')
		print(f[0 : 6])
		print(f)

'''


a = [1, 2, 3, 4, 5, 6, 7, 8, 'leo', 10]
b = (10, 9, 8, 7, 6, 5, 4)
c = (list(b))
a.extend(b)
print(a)
print(a[0], a[len(a)//2], a[-1])

