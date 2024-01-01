class mrk:
    def __init__(self):
        print("               STUDENT MARK LIST         ")
class goat(mrk):
    def get(self):
        self.name=input("enter the student name:")
        self.rollno=int(input("enter the roll no:"))
        print("enter your marks below")
        self.a=int(input("enter tamil mark:"))
        self.b=int(input("enter english mark:"))
        self.c=int(input("enter maths mark:"))
        self.d=int(input("enter python mark:"))
        self.e=int(input("enter C language mark:"))
class tot(goat):
    def yaro(self):
        self.tot=self.a+self.b+self.c+self.d+self.e
        print("your total marks are:",self.tot)
        self.ave=self.tot/5
        print("the average marks is:",self.ave)
class grade(tot):
    def you(self):
        if self.ave>=90:
            print("GRADE O")
        elif self.ave>=80:
            print("GRADE A")
        elif self.ave>=60:
            print("GRADE B")
        elif self.ave>=35:
            print("GRADE C")
        else:
            print("FAIL")
y=grade()
while True:
    print("1. calculation")
    print("2. exit")
    h=int(input("enter your choice:"))
    if h==1:
        y.get()
        y.yaro()
        y.you()
    else:
        exit()








        
        
