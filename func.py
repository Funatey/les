'''
#problem 1

values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
list = []
for i in values:
	try:
		set(i)
		list.append(True)
	except TypeError:
		list.append(False)
print(list)
print(all(list))

#problem 2


set = set()
for i in range(5):
	a = int(input('write numbers: '))
	set.add(a)
print(set)
print(min(set))

#problem 3


a = input('Введите любую функцию Python: ')
try:
	eval(a)
except:
	print('ERROR')

#problem 4

a = int(input('Сумма займа: '))
b = a * (3.47 / 100)
if a > 50000:
	print(f'сумма с процентом {round(b, 2)+ a}')
else:
	print(f'ваш процент{round(b, 2)}сумма должна быть больше 50 000')

#problem 5


try:
	at = 10
	i = 15
	wo = 20

	for e in range(-at, at):
	print(wo / e)
	if at > '5':
	print(at > 5)
except IndentationError:
	print('first')



#problem 6


try:
	a = 0
	b = 1
	numbers = []
	while b > a:
		numbers += b
	b += 1

except TypeError:
        print('<<<TYPE_ERROR>>>')
'''
