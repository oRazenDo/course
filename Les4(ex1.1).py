from pprint import pprint
import random

while input()!='Yes':
    if random.randint(1,2) == 1:
        pprint('Yes')
    else:
        pprint('No')
