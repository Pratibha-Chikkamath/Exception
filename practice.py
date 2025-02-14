#Single level inheritance
class Trainer:
     def teach(self):
       print("hello students")

class Student(Trainer):
    def study(self):
        print("good morning mam")

s=Student()
s.teach()
s.study()
