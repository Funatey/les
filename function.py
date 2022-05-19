# list1 = ['name', 'age', '1', '19']
# def func(a):
#     mid = len(a) // 2
#     b = a[:mid]
#     c = a[mid:]
#     b = list(reversed(b))
#     c = list(reversed(c))
#     return b + c
#
#
# print(func(list1))
list1 = []
pred = 'fawdkan2wwwwwwwww22aoooooooooooooooooAAAAAAAAAAA'
glas = ['e', 'y', 'u', 'i', 'o', 'a', 'E','Y','U','I','O','A']
vowels = 0
for i in pred:
    if i.isalpha():
        if i in glas:
            vowels += 1
            list1.append(i)

print(list1)
print(vowels)