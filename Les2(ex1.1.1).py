YA=[['Bolgov',1998,'Student'],
['Petrov',1996,'Worker'],
['Smirniv',1999,'Student'],
['Oliver',1986,'Teacher'],
['Lucruna',2000,'Student'],
['Kudrina',1997,'Student'],
['Willem',1990,'Worker'],
['Smith',1999,'Student'],
['Nucker',1991,'Worker'],
['Zoop',1998,'Student']]
print("Students:")
for i in YA:
    if i[2] == 'Student':
        print(i[0])
print("Workers:")
for i in YA:
    if i[2] == 'Worker':
        print(i[0])
print("Teachers:")
for i in YA:
    if i[2] == 'Teacher':
        print(i[0])
print('Born 1991 to 1999:')
for i in YA:
    if 1991<=i[1]<=1999:
        print(i[0])

def search_list(list,what_find):
    res=[]
    for i in list:
        for j in i:
            j = str(j)
            if (j == what_find):
                res.append(i)
    return res
name=input('Find: ')
print(search_list(YA,name))
