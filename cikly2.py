'''
#hack password


a = input('ведите 6 значный пароль : ')

while len(a) != 6 or not a.isdigit() : 
	print('False') 
	a = input('ведите 6 значный пароль : ') 

else:
	s = 100000 
	print('ok') 
	while s != int(a): 
		print('пороль не совпал', s) 
		s += 1 
	else:
		print('вы взломали пaроль!!!', s) 
		print(f'вы потратили {s-100000}')


#problem 1
#problem 2

i = 0
languages = ['go', 'java', 'php', 'python', '213','rust','qwerty','pipipi', 'javascript', 'ruby']
while i < len(languages):
	print(languages[i])
	if languages[i] == 'rust':
		print('language is in list')
		break
	i+=1


#problem 3

i = 0
a = 7
while i < 5:
	i+=1
	a*=7
	print(a)

#problem 4


a = 0
b = ['go', 'java', 'php', 'python', '213','rust','qwerty','pipipi', 'javascript', 'ruby']
while a < len(b):
	print(a, b[a])
	if a > len(b):
		break
	a += 1


#problem 5
'''
a = 0
while a <= 10:
	print(a)
	a+=1

