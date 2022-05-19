'''
#problem 1


with open('directories.txt', 'a') as a:
	a.write('lessonsIT/   Видео/   Документы/   Загрузки/   Изображения/   Музыка/   Общедоступные/  Рабочий стол/   Шаблоны/')
	print('завершено')

#problem 2


log = input('add login: ')
pas = input('add password: ')

with open('users.txt', 'a') as r:
	r.write(f'{log} : {pas}')
	r.write('\n')
	print('Finish')

#problem 3

with open('users.txt', 'r') as a:
	b = a.read()
	if 'w' in b:
		print('have w')
	else:
		print('have not w')


#problem 4


t_words = []
with open('grrr.txt', 'r') as a:
	for i in a.read().split():
		if 't' in i or 'T' in i:
			t_words.append(i)
print(f'слова добавлены, {t_words}')

#problem 5
'''
with open('database.txt', 'w') as a:
	a.write('leo : 123; , merei : 321; ,')

enter = input('войти или зарегистрироваться: ')
login = input('ВВедите логин: ')
with open('database.txt', 'r') as b:
	for i in b.read().split():
		if login in i:
			pasword = input('введите пароль: ')
		else:
			print('логин успешно создан!')

password2 = input('введите новый пароль: ')
password3 = input('подтвердите пароль: ')
with open('database.txt', 'a') as c:
	if password2 == password3:
		c.write(f'{login} : {password3}; ')
		print('учетная запись успешно создана и добавлена в базу данных')
	else:
		print('пароли не совпадают!')
