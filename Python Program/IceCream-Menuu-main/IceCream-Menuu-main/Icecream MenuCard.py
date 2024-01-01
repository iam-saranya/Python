class icecream:
    print("********* WELCOME TO ARUN ICECREAM*********")
    def __init__(self,s=0,r=0,p=0,q=0,y=0,e=0):
        self.s=s
        self.r=r
        self.p=p
        self.q=q
        self.y=y
        self.e=0
class bigcup(icecream):
    def bigcups(self):
        print("1. Butterscotch........Rs.40")
        print("2. kesarpista...........Rs.40")
        print("3. mango................Rs.40")
        print("4. blackcurrent.........Rs.40")
        print("5. vennila..............Rs.35")
        print("6. american dry fruits........RS.40")
        print("7. chocolate chips...........RS.45")
        print("8. kaju therax...........Rs.40")
        print("9. straberry.........Rs.45")
        print("10. pista malaai........Rs.45")
        a=int(input("enter the choice:"))
        if a==1:
            b=int(input("enter the quantities:"))
            self.s=self.s+40*b
            print("butterscotch rs",self.s)
        elif a==2:
            b=int(input("enter the quantities:"))
            self.s=self.s+40*b
            print("kesarpista rs",self.s)
        elif a==3:
            b=int(input("enter the quantities:"))
            self.s=self.s+40*b
            print("mango rs",self.s)
        elif a==4:
            b=int(input("enter the quantities:"))
            self.s=self.s+40*b
            print("blackcurrent rs",self.s)
        elif a==5:
            b=int(input("enter the quantities:"))
            self.s=self.s+35*b
            print("vennila rs",self.s)
        elif a==6:
            b=int(input("enter the quantities:"))
            self.s=self.s+40*b
            print("american dry fruits rs",self.s)
        elif a==7:
            b=int(input("enter the quantities:"))
            self.s=self.s+45*b
            print("chocolate chips rs",self.s)
        elif a==8:
            b=int(input("enter the quantities:"))
            self.s=self.s+40*b
            print("kajutherax rs",self.s)
        elif a==9:
            b=int(input("enter the quantities:"))
            self.s=self.s+45*b
            print("straberry",self.s)
        elif a==10:
            b=int(input("enter the quantities:"))
            self.s=self.s+45*b
            print("pista malaai",self.s)
        else:
            print("not available")
class mediumcup(bigcup):
    def mediumcups(self):
        print("1. vennilla.........Rs.25")
        print("2. chocolate........Rs.50")
        w=int(input("enter the choice:"))
        if w==1:
            p=int(input("enter the quantities:"))
            self.r=self.r+25*w
            print("vennila rs",self.r)
        elif w==2:
            p=int(input("enter the quantities:"))
            self.r=self.r+50*w
            print("chocolate rs",self.r)
        else:
            print("not valid")
class smallcup(mediumcup):
    def smallcups(self):
        print("1. vennila..............rs.15")
        print("2. straberry..........rs.15")
        l=int(input("enter the choice:"))
        if l==1:
            c=int(input("enter the quantities:"))
            self.p=self.p+15*c
            print("vennila rs",self.p)
        elif l==2:
            c=int(input("enter the quantities:"))
            self.p=self.p+15*c
            print("straberry rs",self.p)
        else:
            print("not available")
class kulufi(smallcup):
    def kulfi(self):
        print("1. pista kulfi..........Rs.35")
        print("2. kesar kulfi..........Rs.50")
        print("3. malaai kulfi.........Rs.40")
        print("4. badam kulfi..........Rs.35")
        print("5. milk kulfi............Rs.15")
        k=int(input("enter the choice:"))
        if k==1:
            j=int(input("enter the quantities:"))
            self.q=self.q+35*j
            print("pista kulfi rs",self.q)
        elif k==2:
            j=int(input("enter the quantities:"))
            self.q=self.q+50*j
            print("kesar kulfi rs",self.q)
        elif k==3:
            j=int(input("enter the quantities:"))
            self.q=self.q+40*j
            print("malaai kulfi rs",self.q)
        elif k==4:
            j=int(input("enter the quantities:"))
            self.q=self.q+35*j
            print("badam kulfi rs",self.q)
        elif k==5:
            j=int(input("enter the quantities:"))
            self.q=self.q+15*j
            print("milk kulfi rs",self.q)
        else:
            print("not valid")
class cone(kulufi):
    def coneice(self):
        print("1. vennila cone........Rs.45")
        print("2. straberry cone......Rs.40")
        print("3. blackcurrent........Rs.50")
        print("4. chocolate cone...........Rs.45")
        x=int(input("enter the choice:"))
        if x==1:
            u=int(input("enter the quantities:"))
            self.y=self.y+45*u
            print("vennila cone rs",self.y)
        elif x==2:
            u=int(input("enter the quantities:"))
            self.y=self.y+40*u
            print("straberry cone rs",self.y)
        elif x==3:
            u=int(input("enter the quantities:"))
            self.y=self.y+50*u
            print("blackcurrent cone rs",self.y)
        elif x==4:
            u=int(input("enter the quantities:"))
            self.y=self.y+45*u
            print("chocolate cone rs",self.y)
        else:
            print("not valid")
class kuchi(cone):
    def kuchiice(self):
        print("1. semiya.......Rs.11")
        print("2. paal ice.....Rs.10")
        print("3. grape ice......Rs.15")
        print("4. orange ice.......Rs.8")
        i=int(input("enter the quantities:"))
        if i==1:
            g=int(input("enter the choice:"))
            self.e=self.e+11*g
            print("semiya rs",self.e)
        elif i==2:
            u=int(input("enter the choice:"))
            self.e=self.e+10*g
            print("paal ice rs",self.e)
        elif i==3:
            u=int(input("enter the choice:"))
            self.e=self.e+15*g
            print("grape ice rs",self.e)
        elif i==4:
            u=int(input("enter the choice:"))
            self.e=self.e+8*g
            print("orange ice rs",self.e)
        else:
            print("not valid")
class byebye(kuchi):
    def bye(self):
        print("***********THANK YOU VISIT AGAIN****************")
    def display():
        print("bigcups",self.s)
        print("mediumcups",self.r)
        print("smallcups",self.p)
        print("kulfi",self.q)
        print("coneice",self.y)
        print("kuchiice",self.e)
        
k=byebye()
while(1):
    print("1.bigcups\n2.mediumcups\n3.smallcups\n4.kulfi\n5.coneice\n6.kuchiice")
    f=int(input("enter the items:"))
    if(f==1):
        k.bigcups()
    if(f==2):
        k.mediumcups()
    if(f==3):
        k.smallcups()
    if(f==4):
        k.kulfi()
    if(f==5):
        k.coneice()
    if(f==6):
        k.kuchiice()
            
        
        

        
            
            



    

