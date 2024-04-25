import json
from datetime import datetime
import json

def load_expenses():
    # Try to load existing expenses from a JSON file
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

def save_expenses(expenses):
    # Save expenses to a JSON file
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=2)

def log_expense(expenses, category, amount, description):
    # Log a new expense
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if category not in expenses:
        expenses[category] = []  # Create a new category if it doesn't exist
    expenses[category].append({
        'timestamp': timestamp,
        'amount': amount,
        'description': description
    })
    save_expenses(expenses)  # Save the updated expenses

def display_summary(expenses):
    # Display a summary of expenses
    total_expenses = 0
    for category, items in expenses.items():
        total_category_expenses = sum(item['amount'] for item in items)
        total_expenses += total_category_expenses
        print(f"\nCategory: {category}")
        print(f"Total Expenses: ${total_category_expenses}")
        print("Details:")
        for item in items:
            print(f"  - {item['timestamp']} | ${item['amount']} | {item['description']}")
    print("\n-------------------------")
    print(f"Total Expenses: ${total_expenses}")

def main():
    expenses = load_expenses()  # Load existing expenses or create an empty dictionary

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Log Expense")
        print("2. View Summary")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: "))
            description = input("Enter a short description: ")
            log_expense(expenses, category, amount, description)
            print("Expense logged successfully!")

        elif choice == '2':
            display_summary(expenses)

        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
