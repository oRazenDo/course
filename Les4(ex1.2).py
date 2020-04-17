from pprint import pprint
import random

def check_ava(input,list):
    count=0
    for i in list:
        if input==i:
            count+=1
    return count

global_ms=['Gray']
pprint(global_ms)
a=input('If you want exit press + ')
while a!='+':
    if check_ava(a,global_ms)>0:
        pprint('Yes')
    else:
        global_ms.append(a)
        pprint('No')
#    pprint(global_ms)
    a=input()
