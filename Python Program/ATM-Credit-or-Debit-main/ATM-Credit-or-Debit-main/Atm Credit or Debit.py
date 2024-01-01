import time

print("Please insert Your CARD")

#for card processing
time.sleep(5)

password = 1234

#taking atm pin from user
pin = int(input("enter your atm pin:"))

#user account balance
balance = 5000

#checking pin is valid or not 
if pin == password:
    #loop will run user get free 
    while True:

        #Showing  info to user

        print(""" 
			1 == balance
			2 == withdraw 
			3 == deposit 
			4 == exit
			"""
              )

        try:    
             #taking an option from user
            option = int(input("Please enter your choice:"))
        except:
            print("Please enter valid option")
        
        #for option 1        
        if option == 1:
            print("Your current balance is {balance}",balance)
                                     
        if option == 2:

            withdraw_amount = int(input("please enter withdraw_amount: "))

            

            balance = balance - withdraw_amount

            print("{withdraw_amount} is debited from your account",withdraw_amount)

            

            print("your updated balance is {balance}",balance)

            

        if option == 3:

            deposit_amount = int(input("please enter deposit_amount:"))

            balance = balance + deposit_amount

            

            print("{deposit_amount} is credited to your account",deposit_amount)



            print("your updated balance is {balance}",balance)



        if option == 4:
            exit()

            break


else:
    print("wrong pin Please try again")
