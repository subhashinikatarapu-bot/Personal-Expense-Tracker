
expenses = []

def add_expense():
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount (₹): "))
        category = input("Enter category: ")

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }
        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['name']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )

def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expenses: ₹{total:.2f}")

while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
