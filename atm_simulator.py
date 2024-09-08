balance = 1000
max_attempts = 3

current_attempt_number = 0
while current_attempt_number < max_attempts:
    withdrawal_amount = input("Enter the amount to be withdrawn: ")
    withdrawal_amount_int = int(withdrawal_amount)
    if withdrawal_amount_int <= balance and withdrawal_amount_int > 0:
        balance = balance - withdrawal_amount_int
        print(f"The new balance is {balance}")
        break
    else:
        if withdrawal_amount_int < 0:
            print("Invalid amount!")
        if withdrawal_amount_int > balance:
            print("You cannot withdraw the money: Insufficient funds")
    current_attempt_number = current_attempt_number + 1
print("We are out of the loop")
 