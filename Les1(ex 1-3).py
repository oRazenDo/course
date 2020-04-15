print("Задание 1:")
x=18+(1/10)*(30+(33/44)+50+(55/88))/(9/10)
print("1: ",x)
print("2: ",sum(range(0,88888888)))
r=[3,56,100,2,2,3]
print("3: ",sum(r)/len(r))

print("Задание 2:")

xy='sdjggdsgyxtsux xysx yxiosd klsys xx yy'
yy=''
for i in xy:
    if i == 'x':
        yy+='y'
    else:
        yy+=i
print("1: ", yy)
ch=[1, 2, 3, 4, 5, 55, 13, 21, 90, 75, 44]
p=1
for i in ch:
    if i%3==0:
        p*=i
    elif i%5==0:
        p*=i
print("2: ",p)

print("3: ",xy.replace('x','y'))

print("Задание 3:")
YA=['Bolgov','A.S.',1998,'Student']
print('1: ',YA)

YA2 = {'BolgovAS':{'Born in ': 1998,'Specialty': 'Student'}}
print('2: ',YA2)

print('3: Словарь удобнее с точки зрения поиска, информация более структурирована ')
