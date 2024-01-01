class college:
    def __init__(self):
        print("************WELCUM TO ARTS COLLEGE************ ")
        self.name=input("enter the college name:")
        self.dt=input("enter the place:")
class details(college):
    def info(self):
        while(1):
            print("1.student details")
            print("2.college details")
            print("3.show details")
            c=int(input("enter the choice:"))
            if c==1:
                self.nme=input("enter the candidate name:")
                self.ff=input("enter the gender:")
                self.ag=input("enter the age of stdnt:")
                self.db=input("enter the father name:")
                self.gn=input("enter the mother name:")
                self.ty=input("enter the D.O.B:")
                self.oo=input("enter the address:")
                self.op=input("enter the group you studied in class 12th:")
                self.te=input("enter the passed out yr:")
            elif c==2:
                print("********* Courses Offered *********")
                print("1.^^^^ UG Courses ^^^^")
                print("2.^^^^ PG Courses ^^^^")
                r=int(input("enter the course:"))
                if r==1:
                    print("1. B.A-English Literature")
                    print("2. B.B.A-Business Administration")
                    print("3. B.Sc-Computer Science")
                    print("4. B.C.A-Computer Applications")
                    print("5. B.Com-Computer Applications")
                    print("6. B.Sc-Information Systems & mgmt")
                    print("7. B.Sc-Nutrition,Food Service Management & Dietics")
                    print("8. B.Sc-Biotechnology")
                    print("9. B.Sc-Maths")
                    print("10. B.Sc-Interior Design and Decor")
                    t=int(input("enter the course you want:"))
                    if t==1:
                        print(" THANKS FOR CHOOSING BA-ENGLISH")
                        print("the fee structure is RS.20000 per yr")
                        print("the duration of the course if 3 YRS")
                    elif t==2:
                        print(" THANKS FOR CHOOSING BBA")
                        print("the fee structure is RS.25000 per yr")
                        print("the duration of the course if 3 YRS")
                    elif t==3:
                        print(" THANKS FOR CHOOSING B.Sc-Computer Science")
                        print("the fee structure is RS.30000 per yr")
                        print("the duration of the course if 3 YRS")
                    elif t==4:
                        print(" THANKS FOR CHOOSING B.C.A")
                        print("the fee structure is RS.29000 per yr")
                        print("the duration of the course if 3 YRS")
                    elif t==5:
                        print(" THANKS FOR CHOOSING B.Com")
                        print("the fee structure is RS.20000 per yr")
                        print("the duration of the course if 3 YRS")
                    elif t==6:
                        print(" THANKS FOR CHOOSING B.Sc-Information Systems & mgmt")
                        print("the fee structure is RS.22000 per yr")
                        print("the duration of the course if 3 YRS")
                    elif t==7:
                        print(" THANKS FOR CHOOSING B.Sc-Nutrition,Food Service Management & Dietics")
                        print("the fee structure is RS.20000 per yr")
                        print("the duration of the course if 3 YRS")
                    elif t==8:
                        print(" THANKS FOR CHOOSING B.Sc-Biotechnology")
                        print("the fee structure is RS.23000 per yr")
                        print("the duration of the course if 3 YRS")
                    elif t==9:
                        print(" THANKS FOR CHOOSING B.Sc-Maths")
                        print("the fee structure is RS.24000 per yr")
                        print("the duration of the course if 3 YRS")
                    elif t==10:
                        print(" THANKS FOR CHOOSING B.Sc-Interior Design and Decor")
                        print("the fee structure is RS.25000 per yr")
                        print("the duration of the course if 3 YRS")
                    else:
                        print("not valid")
                elif r==2:
                    print("1. M.A-English Literature")
                    print("2. M.A-BioTechnology")
                    print("3. M.Sc-Maths")
                    print("4. M.Sc-Computer Science")
                    print("5. M.Com-Commerce")
                    d=int(input("enter the course you want:"))
                    if d==1:
                        print(" THANKS FOR CHOOSING MA-English Literature")
                        print("the fee structure is RS.35000 per yr")
                        print("the duration of the course if 2 YRS")
                    elif d==2:
                        print(" THANKS FOR CHOOSING M.A-BioTechnology")
                        print("the fee structure is RS.30000 per yr")
                        print("the duration of the course if 2 YRS")
                    elif d==3:
                        print(" THANKS FOR CHOOSING M.Sc-Maths")
                        print("the fee structure is RS.29000 per yr")
                        print("the duration of the course if 2 YRS")
                    elif d==4:
                        print(" THANKS FOR CHOOSING M.Sc-Computer Science")
                        print("the fee structure is RS.34000 per yr")
                        print("the duration of the course if 2 YRS")
                    elif d==5:
                        print(" THANKS FOR CHOOSING M.Com-Commerce")
                        print("the fee structure is RS.30000 per yr")
                        print("the duration of the course if 2 YRS")
                    else:
                        print("not valid")
            elif c==3:
                print(self.name)
                print(self.dt)
                print(self.nme)
                print(self.ff)
                print(self.ag)
                print(self.db)
                print(self.gn)
                print(self.ty)
                print(self.oo)
                print(self.op)
                print(self.te)
                
            else:
                print("not valid")
class over(details):
    def bb(self):
        print("visit us again :)")
w=over()
w.info()
w.bb()
                    
                    
                    
                    
                    
                    
                    
                
                                                                                               
        
