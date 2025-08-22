#no 12 task2
#mock ussd interface
print("Welcome to Nija Service Provider")
Ussd_code = input("please dial a code (eg., *556#):")
if Ussd_code == "*556#":
    print("\nMenu:")
    print("1. Check balance")
    print("2. Buy Airtime")
    print("3. Buy Data")

    choice = input("\nEnter your choice (1, 2, 3): ")

    if choice == "1":
        print(f"\nYou selected: Check Balance!")
        print("Your current balance is #100000. Thank you")

    elif choice == "2":
         print(f"\nYou selected: Buy Airtime")
         Amount = int(input("Enter Amount of airtime to buy: #"))
         print(f"You have successfully purshased #{Amount} airtime. Thank you!")
    elif choice == "3":
        print(f"\nYou selected: Buy Data")
        Amount = int(input("Enter amount of data boundle(#):"))
        print(f"You have successfully purshaced a data boundle worth #{Amount}. Thank you!")
    else: print("invalid option. pleace try again.")
else:
    print("\ninvalid USSD code. please dial *556# to continue.")