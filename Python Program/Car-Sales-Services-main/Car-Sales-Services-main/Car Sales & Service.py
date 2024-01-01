class car:
    def __init__(self):
        print(":)NAMBI VAANGA(:")
        self.name=input("enter the name:")
        self.phno=int(input("enter the phone no:"))
class info(car):
    def infoo(self):
        print("1.car sales")
        print("2.car service")
        print("3.exchange offer")
        a=int(input("enter your choice:"))
        if a==1:
            print("1.FORD")
            print("2.AUDI")
            print("3.BMW")
            b=int(input("enter your choice:"))
            if b==1:
                print("THANK YOU FOR CHOOSING FORD")
                print("the bill amount is  Rs:5.82L")
                print("the guarantee card will be provided for 2 YRS")
            elif b==2:
                print("THANK YOU FOR CHOOSING AUDI")
                print("the bill amount is  Rs:Rs. 2.04 Cr*")
                print("the guarantee card will be provided for 2 YRS")
            elif b==3:
                print("THANK YOU FOR CHOOSING BMW")
                print("the bill amount is  Rs:45.40L")
                print("the guarantee card will be provided for 2 YRS")
            else:
                print("enter the valid option")
        elif a==2:
            print("1.FORD")
            print("2.AUDI")
            print("3.BMW")
            c=int(input("enter your choice:"))
            if c==1:
                print("the service amount bill is RS.10000")
            elif c==2:
                print("the service amount bill is RS.50000")
            elif c==3:
                print("the service amount bill is RS.70000")
            else:
                print("enter the valid option")
        elif a==3:
            print("1. 1 to 3 years")
            print("2. 4 to 7 years")
            print("3. 7 and above")
            d=int(input("enter your choice:"))
            if d==1:
                print("welcome by yazhini")
                amount=int(input("enter the car amount:"))
                rate=amount*0.8
                print("the car exchange amount is:",rate)
            elif d==2:
                print("welcome by preethika")
                amount=int(input("enter the car amount:"))
                rate=amount*0.6
                print("the car exchange amount is:",rate)
            elif d==3:
                print("welcome by saranya")
                amount=int(input("enter the car amount:"))
                rate=amount*0.4
                print("the car exchange amount is:",rate)
            else:
                print("enter the valid option")
        else:
            print("enter the valid option")
class chuma(info):
    def bye(self):
        print("      THANK YOU ._.")
        print("   VISIT US AGAIN")
z=chuma()
z.infoo()
z.bye()
                
