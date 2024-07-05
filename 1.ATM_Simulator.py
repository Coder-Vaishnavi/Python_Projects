import time

print('Please Insert your ATM Card')
time.sleep(5)

pin = input("Enter your 4 digit ATM Pin: ")
balance = 1000

if pin == '1234':
    while True:
        print("1 = Check Balance")
        print("2 = Withdraw Money")
        print("3 = Deposit Money")
        print("4 = Exit")
        
        try:
            option = int(input("Choose an Option: "))
        except ValueError:
            print("Invalid Option. Please choose a valid option.")
            continue
        
        if option == 1:
            print("-------------------")
            print(f"Your Current Balance is {balance}")
        elif option == 2:
            withdraw_money = int(input("Enter Your Withdraw Amount: "))
            if withdraw_money > balance:
                print("Insufficient Balance. Transaction canceled.")
            else:
                balance -= withdraw_money
                print("-------------------")
                print(f"{withdraw_money} is debited from your account.")
                print(f"Your Current balance is {balance}")
        elif option == 3:
            deposit_money = int(input("Enter the Deposit Amount: "))
            balance += deposit_money
            print("-------------------")
            print(f"{deposit_money} is credited to your account.")
            print(f"Your Current balance is {balance}")
        elif option == 4:
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid Option. Please choose a valid option.")
else:
    print('Wrong Pin')
