class student:
    def __init__ (self,rollno,name,course):
        self.rollno = rollno
        self.name = name
        self.course = course
    def display(self):
        print("my Roll Number is "+str(self.rollno))
        print("my Name is "+str(self.name))
        print("my Course is "+str(self.course))
s1 = student(101,"John","AI&DS")
s1.display()
s2 = student(102,"Raj","CSBS")
s2.display() 
