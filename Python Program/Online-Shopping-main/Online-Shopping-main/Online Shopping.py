class cloth:
    def __init__(self):
        print("WELCOME TO DOLPHINE CLOTHS")
        self.a=input("enter the name:")
        self.phone=input("enter the phone no:")
        self.address=input("enter the correct address:")
        self.mail=input("enter the mailid:")
class hai(cloth):
    def heloo(self):
        while(1):
            print("1.womens cloth collection")
            print("2.mens cloth collection")
            print("3.childrens cloth collection")
            print("4.exit")
            b=int(input("enter your choice:"))
            if b==1:
                print("1.kurthi..............RS.2000")
                print("2.jeans and tops..............RS.3500")
                print("3.sarees and blouse..............RS.8000")
                print("4.inners................RS.1000")
                c=int(input("enter the option:"))
                if c==1:
                    print("the bill amount is RS.2000")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                elif c==2:
                    print("the bill amount is RS.3500")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                elif c==3:
                    print("the bill amount is 8000")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                elif c==4:
                    print("the bill amount is 1000")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                else:
                    print("not valid")
            elif b==2:
                print("1.formals.................RS.3000")
                print("2.casuals................RS.4500")
                print("3.inners................RS.1500")
                d=int(input("enter the choice:"))
                if d==1:
                    print("the bill amount is RS.3000")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                elif d==2:
                    print("the bill amount is RS.4500")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                elif d==3:
                    print("the bill amount is RS.1500")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                else:
                    print("not valid")
                    
            elif b==3:
                print("1.frock..........RS.2000")
                print("2.shirt & pants & toursers..........RS.8000")
                print("3.inners...................RS.1500")
                e=int(input("enter the choice:"))
                if e==1:
                    print("the bill amount is RS.2000")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                elif e==2:
                    print("the bill amount is RS.8000")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                elif e==3:
                    print("the bill amount is RS.1500")
                    print("          THANKS FOR SHOPPING         ")
                    print("          ._. VISIT AGAIN ._.       ")
                else:
                    print("not valid")
            elif b==4:
                exit()
            else:
                print("not valid")
class bye(hai):
    def byebye(self):
        print("          THANKS FOR SHOPPING         ")
        print("          ._. VISIT AGAIN ._.       ")
t=bye()
t.heloo()
t.byebye()


            
            
        
