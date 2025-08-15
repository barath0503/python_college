# Write a python program to check if a number is divisible by both 3 and 5
def q1():
    n = int(input("Enter a number: "))
    if n % 3 == 0 and n % 5 == 0:
        print("It is divisible by both 3 and 5")
    else:
        print("It is not divisible by both 3 and 5")


# Write a python program to print all even numbers between 1 and 20
def q2():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)


# Print numbers from 1 to 10 but skip when it reaches 6
def q3():
    for i in range(1, 11):
        if i == 6:
            continue
        print(i)


# Print numbers from 1 to 10 skipping multiples of 3
def q4():
    for i in range(1, 11):
        if i % 3 == 0:
            continue
        print(i)
#atm func
def withdraw(w_amount, Balance, T_history):
    if w_amount > Balance:
        print("Amount exceeds balance")
        print("CHECK YOUR BALANCE!!")
    elif w_amount % 100 != 0:
        print("Amount not in multiples of 100")
        print("RETRY")
    else:
        Balance -= w_amount
        print(f"Money withdrawn: {w_amount}")
        T_history.append((w_amount, -1))
    return Balance


def deposit(d_amount, Balance, T_history):
    if d_amount <= 0:
        print("INVALID ENTRY!!")
    else:
        Balance += d_amount
        T_history.append((d_amount, 1))
        print(f"Money Deposited: {d_amount}")
    return Balance


def atm():
    password = 123456
    Balance = 3000
    not_exit = True
    T_history = []

    print("WELCOME!!")
    for _ in range(3):
        pin = int(input("Enter your six digit pin: "))
        if pin == password:
            break
        else:
            print("WRONG PIN.TRY AGAIN!!")
    else:
        print("Too many wrong attempts. Exiting...")
        return

    if pin == password:
        while not_exit:
            print("\nMenu:\n1) Check Balance\n2) Withdraw Money\n3) Deposit Money\n4) Last 5 transaction history\n5) Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(f"Your current Balance: {Balance}")

            elif choice == 2:
                w_amount = int(input("Enter the withdrawal amount: "))
                Balance= withdraw(w_amount, Balance, T_history)

            elif choice == 3:
                d_amount = int(input("Enter the deposit amount: "))
                Balance= deposit(d_amount, Balance, T_history)

            elif choice == 4:
                print("Last 5 transaction history:")
                if not T_history:
                    print("No transactions found")
                else:
                    last_5 = T_history[-5:]
                    for amt, t_type in last_5:
                        if t_type == -1:
                            print(f"Withdrawn: {amt}")
                        else:
                            print(f"Deposited: {amt}")

            elif choice == 5:
                not_exit = False
                print("Exited!!")

            else:
                print("Invalid choice. Try again.")

atm()