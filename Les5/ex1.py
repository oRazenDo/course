class People():

    def __init__(self, name, age, speciality):
        self.name = name
        self.age = age
        self.speciality = speciality

class Student(People):
    def __init__(self,name, age, speciality, gradeStud ):
        super().__init__(name, age, speciality)
        self.gradeStud = gradeStud
    def where(self):
        return "%s in class" % self.name
    def rank(self):
        return "Rank %s as a %s is %s" % (self.name, self.speciality, self.gradeStud)
    def pay(self):
        self.gradeStud = self.gradeStud*10
        return "Pay is %s" % self.gradeStud

class Teacher(People):
    def __init__(self,name, age, speciality, gradeTeach ):
        super().__init__(name, age, speciality)
        self.gradeTeach = gradeTeach
    def where(self):
        return "%s at work" % self.name
    def rank(self):
        return "Rank %s as a %s is %s" % (self.name, self.speciality, self.gradeTeach)
    def pay(self):
        self.gradeTeach = self.gradeTeach*100
        return "Pay is %s " % self.gradeTeach

fonk = Student('Fonk',22,'student',4)
print(fonk.where())
print(fonk.rank(),'and',fonk.pay())
grace = Teacher('Grace',35,'teacher',8)
print(grace.where())
print(grace.rank(),'and',grace.pay())
wizzy = People('Wizzy',29,'student')
print(wizzy.where())
