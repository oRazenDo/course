
YA = {1:{'Name':'Bolgov','Born in ': 1998,'Specialty': 'Student'},
        2:{'Name':'Petrov','Born in ': 1996,'Specialty': 'Worker'},
        3:{'Name':'Smirniv','Born in ': 1999,'Specialty': 'Student'},
        4:{'Name':'Oliver','Born in ': 1986,'Specialty': 'Teacher'},
        5:{'Name':'Lucruna','Born in ': 2000,'Specialty': 'Student'},
        6:{'Name':'Kudrina','Born in ': 1997,'Specialty': 'Student'},
        7:{'Name':'Willem','Born in ': 1990,'Specialty': 'Worker'},
        8:{'Name':'Smith','Born in ': 1999,'Specialty': 'Student'},
        9:{'Name':'Nucker','Born in ': 1991,'Specialty': 'Worker'},
        10:{'Name':'Zoop','Born in ': 1998,'Specialty': 'Student'}}
print("Students:")
for i in YA:
    if YA[i]['Specialty'] == 'Student':
        print(YA[i]['Name'])
print('Born 1991 to 1999:')
for i in YA:
    if 1991 <= YA[i]['Born in '] <= 1999:
        print(YA[i]['Name'])
print("Workers:")
for i in YA:
    if YA[i]['Specialty'] == 'Worker':
        print(YA[i]['Name'])
print("Teachers:")
for i in YA:
    if YA[i]['Specialty'] == 'Teacher':
        print(YA[i]['Name'])
name = input("Find name: ")
for i in YA:
    if YA[i]['Name'] == name:
        print(YA[i])
