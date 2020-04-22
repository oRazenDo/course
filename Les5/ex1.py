class Whois():

    def __init__(self, name, age, speciality, grade):
        self.name = name
        self.age = age
        self.speciality = speciality
        self.grade = grade

    def where(self):
        if self.speciality == 'student':
            return "%s in class" % self.name
        elif self.speciality == 'teacher':
            return "%s at work" % self.name

    def rank(self):
        return "rank %s as a %s is %s" % (self.name, self.speciality, self.grade)

fonk = Whois('Fonk',22,'student',4)
print(fonk.where())
print(fonk.rank())
grace = Whois('Grace',35,'teacher',8)
print(grace.where())
print(grace.rank())
