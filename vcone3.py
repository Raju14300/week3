import csv
import os
from datetime import datetime
EXPENSE_FILE = "expenses.csv"
def initialize_file():
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
def add_expense():
    try:
        date = datetime.today().strftime('%Y-%m-%d')
        category = input("Enter category (Food, Transport, Entertainment, etc.): ").strip()
        amount = float(input("Enter amount: "))
        description = input("Enter description: ").strip()
        with open(EXPENSE_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
def view_expenses():
    try:
        with open(EXPENSE_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader, None)  
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded yet.")
            return

        for expense in expenses:
            print(f"Date: {expense[0]}, Category: {expense[1]}, Amount: {expense[2]}, Description: {expense[3]}")
    except FileNotFoundError:
        print("Expense file not found.")
def expense_summary():
    try:
        category_totals = {}
        monthly_total = 0
        current_month = datetime.today().strftime('%Y-%m')
        with open(EXPENSE_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if len(row) != 4:
                    continue  
                date, category, amount, _ = row
                try:
                    amount = float(amount)
                except ValueError:
                    continue  
                if date.startswith(current_month):
                    monthly_total += amount
                    category_totals[category] = category_totals.get(category, 0) + amount
        print(f"Total expenses for {current_month}: ${monthly_total:.2f}")
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")
    except FileNotFoundError:
        print("Expense file not found.")
def main():
    initialize_file()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
