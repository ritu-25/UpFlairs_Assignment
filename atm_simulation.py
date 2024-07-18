# <<<<<<<<<<<< using  Nested If Else Condition >>>>>>>>------->>>>>
name = input("Plz enter your name : ")
print("Hello ",name)

message = '''
How may i help you sir ...

Please select any of them option ..
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT .
Type 3 >>>> WITHDRAW .
'''
print(message)
task = int(input('Plz enter your options : '))
available_amount = 5000

if task >= 1 and task <= 3:
    print("Welcome to you in virtual bank program")

    if task == 1:
        # Check balance program
        print("Your available amount is : ", available_amount, 'INR')

    elif task == 2:
        # Deposit ammount program
        deposite_amount = int(input("Plz enter deposite amount : "))

        if deposite_amount > 0:
            # available_amount = available_amount + deposite_amount
            available_amount += deposite_amount
            print("You have successfully Deposited your amount : ",deposite_amount)
            print("Your available amount is : ", available_amount, 'INR')


        else:
            print("Plz enter valid amount ! ")

        

    else:
        # Withdral amount program
        withdral_amount = int(input("Plz enter withdral amount : "))

        if withdral_amount <= available_amount:
            available_amount -= withdral_amount
            print("You have successfully withdral your amount : ",withdral_amount)
            print("Your available amount is : ", available_amount, 'INR')

        else:
            print("You don't have an sufficient amount in your account ! ")

        
else:
    print("Please choose a valid option in between 1 tp 3 !")




# same program 3