a = input('creat login: ')
b = input('creat password: ')
c = input('repit password: ')

if not a.isalpha() and not a.isdigit():
       print ('Логин принят')
	if b == c:
		print ('пароль подтвержден')
		print ('user= {a}, {b}, cохранен')
        else:
             	print ('пароль не совпадает')
else:
     	print ('логин должен состоять из букв и цифр')












'''
problem 0

a = ['dadada', 'nenene', 'nonono', 'yesyesyes', 'dwadawd']
print (a)
problem 1

a = ('yes', 'maybe', 'no')
print (a[0], a[1], a[2])

problem 2

a = ['10', '4.5', 'work', 'True']
print (a)

problem 3




names = ['Seku ', 'Vika ', 'Ali ', 'Erbol ', 'Bratya ']

print (names.join)


problem 4

a = ['1', '2', '3']
b = ['4', '5', '6']
a.extend(b)
print (a)

problem 5

names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',
'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',
'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
count = names.count('Jack')
print (count)

problem 6


names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',
'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',
'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
count = names.remove('Jack')
print (names)

problem 7





a = ['Leo', '2001', 'python']

problem 8


a = ["int", "str", "bool", "if", "else", "elif", "loop", 
"tuple", "list", "None", True, False]
print (a)
print (a.index('loop'))
b = a.pop(6)
print (a)

''' 








