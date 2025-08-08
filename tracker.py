from datetime import datetime
# function
def add_expense(amount, description):
    with open("expenses.txt", "a") as file:
        date = datetime.now().strftime("%Y-%m-%d")
        file.write(f"{date},{amount},{description}\n")
    print("Expense added successfully.")

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No expenses recorded.")
                return
            total = 0
            print("\nDate\t\tAmount\tDescription")
            print("-" * 40)
            for line in lines:
                date, amount, description = line.strip().split(",")
                print(f"{date}\t₹{amount}\t{description}")
                total += float(amount)
            print("-" * 40)
            print(f"Total Spent: ₹{total}")
    except FileNotFoundError:
        print("No expenses recorded.")

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        try:
            amount = float(input("Enter amount: ₹"))
            description = input("Enter description: ")
            add_expense(amount, description)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
