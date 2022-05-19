'''
a = list(range(10))
print(a)
print(a[2:10:2])


a = list(range(2,200,2))
print(a)


for i in range(0,200,5):
	print(i)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in a:
	print(i)


for i in range(20):
	for w in range(1, 3):
		print(i,w)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for e in a:
	if e == 8:
		a.append(228)
		print(a)
		if len(a) > 10:
			print(a)


problem 1


languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
a = 'rust'
for e in languages:
	if e == a:
		print('this language is in list')
	else:
		print()

problem 2

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for e in languages:
	print(e)
	if e  == 'php':
		break

problem 3


a = 7
for e in range(0,5,1):
	a *=7
	print(a)

problem 4

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for w in languages:
		print(languages.index(w), w, languages)

problem 5


for e in range(-10,10):
	print(abs(abs(e)-10), end = '|')


problem 6

names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
names2 = []
for i in range(len(names)):
	if i % 2 == 0:
		names2.append(names[i])
		print(i,names2)

problem 7



names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
a = names[0:13:2]
print(a)

problem 8

a = 999
print(a)
if len(str(a)) == 3:
	print('это трехзначное число')
	if a > 0 and a % 2 == 0:
		print('это положительное и четное число')
		if a % 31 == 0:
			print('делится на 31 без остатка')
			if a > 100 and a % 17 == 0 or a > 150 and a == 13**2:
				print(a)


problem 9

a = []
b = []
for i in range(-100, 100):
    if i % 13 == 0 and i % 2 == 0:
        s = i ** 2
        a.append(s)
        
    
    if i % 7 == 0 and i % 2 != 0:
        b.append(i)
        
print(a)
print(b)

#tablica


for b in range(0,13):
	for a in range(0,61):
		print(f'{b} день {a} часов')
		for i in range(0,2):
			for j in range(0,2):
				print(f'{i} * {j} = {i * j}')


'''
