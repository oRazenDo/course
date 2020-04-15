from pprint import pprint

class Person:
    def __init__(self, name, age, specialty):
        self.name, self.age, self.specialty = name, age, specialty
        self.key = (name, specialty)
    def __repr__(self):
        return "Person ('%s','%s','%s')" % (self.name, self.age, self.specialty)

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
pprint(people)
pprint(people[bolgov.key])
