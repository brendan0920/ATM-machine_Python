def main():
    print("**Welcome to ATM**")
    bank = get_bank()
    deposit = get_deposit()
    withdraw = get_withdraw()
    balance = deposit - withdraw
    message = f" \nYOUR TRANSACTION BELOW:\n On your '{bank.upper()}' account:\n Deposited: ${deposit:.2f}\n Withdrawn: ${withdraw:.2f}\n Net Available Balance: ${balance:.2f}\n"
    print(message)
    ask_transaction()


def get_bank():
    while True:
        try:
            bank_list = ["chase", "wells fargo", "bank of america", "boa", "citi bank", "citi", "us bank", "u.s bank"]
            bank_input = input("Enter Your Bank: ").casefold().strip()
            if bank_input in bank_list:
                return bank_input
            else:
                print("Choose from 5 major banks as following: Chase, Wells Fargo, Bank of America, Citi Bank, US bank")
        except ValueError:
            print("Choose from 5 major banks as following: Chase, Wells Fargo, Bank of America, Citi Bank, US bank")


def get_deposit():
    while True:
        try:
            deposit_input = float(input("Amount to be Deposited: "))
            if deposit_input >= 0:
                return deposit_input
            else:
                print("Invalid Amount")
        except ValueError:
            print("Invalid Amount")


def get_withdraw():
    while True:
        try:
            withdraw_input = float(input("Amount to Withdraw: "))
            if withdraw_input >= 0:
                return withdraw_input
            else:
                print("Invalid Amount")
        except ValueError:
            print("Invalid Amount")


def ask_transaction():
    while True:
        retry_msg = input("Do you want another transaction? Yes/No ").casefold().strip()
        yes = ["yes", "y"]
        no = ["no", "n"]
        if retry_msg in yes:
            return main()
        elif retry_msg in no:
            print("***Thanks for using our ATM! Have a Wonderful Day!***")
            break
        else:
            print("Invalid Message, Pelase Type Yes or No")


if __name__ == "__main__":
    main()