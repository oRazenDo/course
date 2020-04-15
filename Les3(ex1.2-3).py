from pprint import pprint
from itertools import product

ALL_WORDS = {'имя','возраст','младше','он','?','все','кто','старше','звали','много',' ли'}

def compare(s1, s2):
    s1, s2 = [ s.lower() for s in [s1,s2] ]
    ngrams = [ s1[i:i+3] for i in range(len(s1)-1) ]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1),len(s2))

def int_val(s):
    try:
        return int(s)
    except ValueError:
        return 0

class Person:
    def __init__(self, name, age, specialty):
        self.name, self.age, self.specialty = name, age, specialty
        self.key = (name, specialty)

    def __repr__(self):
        return "Person ('%s','%s','%s')" % (self.name, self.age, self.specialty)

    def __eq__(self, obj):
        if type(obj) == Person:
            return (self.name, self.age, self.specialty) == (obj.name, obj.age, obj.specialty)
        elif type(obj) == str:
            return self.__fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()

    def __fuzzy_compare(self, query):
        def by_specialty(Q):
            Q = Q - ALL_WORDS
            W = set(self.specialty.replace(',','').split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
            return max(rez)[0]

        def by_age(Q):
            query_age = max([ int_val(q) for q in Q ])
            if 'старше' in Q:
                return query_age < self.age
            if 'младше' in Q:
                return query_age > self.age
            return query_age + 5 >= self.age >= query_age - 5

        def by_name(Q):
            Q = Q - ALL_WORDS
            W = set(self.name.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
            return max(rez)[0]

        q_word = set(query.split())
        score = 0
        for words, method in zip([ALL_WORDS, ALL_WORDS, ALL_WORDS], [by_specialty, by_age, by_name]):
            if words & q_word:
                score +=method(q_word)
        return score > 0.49

bolgov = Person('Bolgov',22,'Student')
petrov = Person('Petrov',24,'Worker')
smirnov = Person('Smirniv',21,'Student')
oliver = Person('Oliver',34,'Teacher')
lucruna = Person('Lucruna',20,'Student')
kudrina = Person('Kudrina',23,'Student')
willem = Person('Willem',30,'Worker')
smith = Person('Smith',21,'Student')
nucker = Person('Nucker',29,'Worker')
zoop = Person('Zoop',22,'Student')

people = {
    bolgov.key: bolgov,
    petrov.key: petrov,
    smirnov.key: smirnov,
    oliver.key: oliver,
    lucruna.key: lucruna,
    kudrina.key: kudrina,
    willem.key: willem,
    smith.key: smith,
    nucker.key: nucker,
    zoop.key: zoop,
}
what_find =[
'имя Oliver',
'возраст младше 30',
'он Teacher ?',
'все кто старше 22',
'звали boltov',
'Person (Petrov,24,Worker)',
'много ли Student ?'
]

for q, p in product(what_find, people.values()):
    if q == p:
        pprint((q, p))
