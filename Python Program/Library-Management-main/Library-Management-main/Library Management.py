class library:
    def __init__(self,cardno=100,name=' ',age=0,gender=' ',phno=0,proof=' ',b=0,c=' ',c1=' ',d=0,d1=0,e=' ',e1=' '):
        print("      WELCOME TO MANI LIBRARY")
        self.cardno=cardno
        self.name=name
        self.age=age
        self.gender=gender
        self.phno=phno
        self.proof=proof
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.c1=c1
        self.d1=d1
        self.e1=e1
class book(library):
    def details(self):
        self.name=input("NAME:")
        self.age=int(input("AGE:"))
        self.gender=input("GENDER:")
        self.cardno+=1
        self.phno=int(input("PHONE NUMBER:"))
        self.proof=input("PROOF WHICH YOU SUBMITTED:")
        print("CARD NUMBER:",self.cardno)
        print("RULES TO BE FOLLOWED")
        print("1.Maintain silence inside the library")
        print("2.Must bring library card while taking book")
        print("3.Can take only 3 books at a time")
        print("4.Not returning book on time,then need to pay RS.2 for each day")
class bk(book):
    def show(self):
        print("1.history books")
        print("2.science books")
        print("3.story books")
        print("4.astronomy")
        print("5.statistics")
        a=int(input("enter the choice:"))
        if a==1:
            print("1.the guns of august")
            print("2.the liberation trilogy")
            print("3.the crusades")
            self.b=int(input("enter the choice"))
            if self.b==1:
                print("u have choosen the guns of august")
            elif self.b==2:
                print("u have choosen the liberation trilogy")
            elif self.b==3:
                print("u have choosen the crusades")
            else:
                print("not valid")
        elif a==2:
            print("1.the gene")
            print("2.the immortal life")
            print("3.a brief history")
            self.b=int(input("enter the choice"))
            if self.b==1:
                print("u have choosen the gene ")
            elif self.b==2:
                print("u have choosen the immortal life")
            elif self.b==3:
                print("u have choosen a brief history")
            else:
                print("not valid")
        elif a==3:
            print("1.the pilgrims")
            print("2.robinson crusor")
            print("3.guliller travels")
            self.b=int(input("enter the choice"))
            if self.b==1:
                print("u have choosen the pilgrims ")
            elif self.b==2:
                print("u have choosen robinson crusor ")
            elif self.b==3:
                print("u have choosen guliller travels ")
            else:
                print("not valid")
            
        elif a==4:
            print("1.Galileo Galilei. NASA")
            print("2.Isaac Newton")
            print("3.Christiaan Huygens")
            self.b=int(input("enter the choice"))
            if self.b==1:
                print("u have choosen Galileo Galilei. NASA ")
            elif self.b==2:
                print("u have choosen Isaac Newton ")
            elif self.b==3:
                print("u have choosen  Christiaan Huygens")
            else:
                print("not valid")
        elif a==5:
            print("1.Nominal data")
            print("2.Ordinal data")
            print("3.Interval data")
            self.b=int(input("enter the choice"))
            if self.b==1:
                print("u have choosen Nominal data ")
            elif self.b==2:
                print("u have choosen  Ordinal data")
            elif self.b==3:
                print("u have choosen  Interval data")
            else:
                print("not valid")
        else:
            print("not valid")
class add(bk):
    def ad(self):
        self.c1=[]
        self.d1=[]
        self.e1=[]
        self.f=int(input("No of books going to add:"))
        for i in range(1,self.f+1,1):
            self.c=input("NAME:")
            self.d=int(input("CARD NUMBER:"))
            self.e=input("BOOK NAME:")
            self.c1.append(self.c)
            self.d1.append(self.d)
            self.e1.append(self.e)
class display(add):
    def dis(self):
        j=0
        for i in range(1,self.f+1,1):
            
            print("NAME OF THE PERSON WHO ADDED THE BOOK:",self.c1[j])
            print("CARD NUMBER:",self.d1[j])
            print("BOOK NAME:",self.e1[j])
            j+=1
o=display()
while True:
    print("1.NEW LIBRARY ACCOUNT")
    print("2.AVAILABLE BOOKS")
    print("3.ADDING BOOKS")
    print("4.DISPLAYING THE ADDED BOOKS")
    print("5.EXIT")
    w=int(input("enter your choice:"))
    if w==1:
        o.details()
    elif w==2:
        o.show()
    elif w==3:
        o.ad()
    elif w==4:
        o.dis()
    elif w==5:
        exit()
    else:
        print("enter the valid option")
            
        
        
