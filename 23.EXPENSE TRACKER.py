# Expense Tracker Project
expenses = []
print("Welcome to the Expense Tracker!")

while True: 
    print("=====MENU=====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

# Add Expenses

    if choice == '1':
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Transport): ")
        description = input("Enter a description: ")
        amount = float(input("Enter the amount: "))

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }
        expenses.append(expense)
        print("\nExpense added successfully!")

# View All Expenses

    elif choice == '2':
        if not expenses:
            print("\nNo expenses recorded.")
        else:
            print("\nAll Expenses:")
            for idx, expense in enumerate(expenses, start=1):
                print(f"{idx}. Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: ${expense['amount']:.2f}")

# View Total Expenses
    elif choice == '3':
        total = sum(expense['amount'] for expense in expenses)
        print(f"\nTotal Expenses: ${total:.2f}")



# Exit
    elif choice == '4':
        print("Thank you for using the Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
        
