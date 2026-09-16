
class Student:
    def __init__(self):
        self.s_name=input("enter your name")
        self.s_rollno=101

    def getdata(self):
            self.s_mb= 240105132088
obj=Student()
obj.getdata()
obj.s_branch="cs"
del obj.s_rollno
print(obj.__dict__)

