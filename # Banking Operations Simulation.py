# Banking Operations Simulation
# This script simulates basic bank transactions like checking balance, deposits, withdrawals, and transfers.

# Initialize balances
current_balance = 0
savings_balance = 0

# Function to view account balance
def view_balance(account_type, current_balance, savings_balance):
    if account_type == "savings":
        balance = savings_balance
    elif account_type == "current":
        balance = current_balance
    else:
        return "Error: Invalid account type. Please select 'current' or 'savings'."

    balance_info = f"The balance in your {account_type} account is {balance} units."
    return balance_info

# Function to deposit money
def deposit_money(account_type, amount, current_balance, savings_balance):
    result = ""
    if amount > 0:
        if account_type == "savings":
            savings_balance += amount
            result = "Deposit successful."
        elif account_type == "current":
            current_balance += amount
            result = "Deposit successful."
        else:
            result = "Error: Invalid account type."
    else:
        result = "Error: Deposit amount must be greater than zero."

    print(f"{result} {amount} units added to your {account_type} account.")
    return current_balance, savings_balance

# Function to withdraw money
def withdraw_money(account_type, amount, current_balance, savings_balance):
    message = ""
    if account_type == "savings":
        if amount <= savings_balance:
            savings_balance -= amount
            message = "Withdrawal successful."
        else:
            message = "Error: Insufficient funds in savings account."
    elif account_type == "current":
        if amount <= current_balance:
            current_balance -= amount
            message = "Withdrawal successful."
        else:
            message = "Error: Insufficient funds in current account."
    else:
        message = "Error: Invalid account type."

    print(f"{message} {amount} units withdrawn from your {account_type} account.")
    return current_balance, savings_balance

# Function to transfer funds between accounts
def transfer_funds(from_account, to_account, amount, current_balance, savings_balance):
    transfer_status = ""

    if from_account == "savings" and to_account == "current":
        if amount <= savings_balance:
            savings_balance -= amount
            current_balance += amount
            transfer_status = "Transfer successful."
        else:
            transfer_status = "Error: Insufficient savings balance for transfer."

    elif from_account == "current" and to_account == "savings":
        if amount <= current_balance:
            current_balance -= amount
            savings_balance += amount
            transfer_status = "Transfer successful."
        else:
            transfer_status = "Error: Insufficient current balance for transfer."

    else:
        transfer_status = "Error: Invalid account types for transfer."

    print(f"{transfer_status} {amount} units transferred from {from_account} to {to_account}.")
    return current_balance, savings_balance

# Example operations
# Viewing balances
print(view_balance("current", current_balance, savings_balance))
print(view_balance("savings", current_balance, savings_balance))

# Depositing money
current_balance, savings_balance = deposit_money("savings", 50, current_balance, savings_balance)
current_balance, savings_balance = deposit_money("current", 200, current_balance, savings_balance)

# Withdrawing money
current_balance, savings_balance = withdraw_money("savings", 20, current_balance, savings_balance)
current_balance, savings_balance = withdraw_money("current", 50, current_balance, savings_balance)

# Transferring funds
current_balance, savings_balance = transfer_funds("savings", "current", 10, current_balance, savings_balance)
current_balance, savings_balance = transfer_funds("current", "savings", 30, current_balance, savings_balance)

# Viewing final balances
print(view_balance("current", current_balance, savings_balance))
print(view_balance("savings", current_balance, savings_balance))
