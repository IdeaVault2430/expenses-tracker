import os
import pandas as pd 
from tabulate import tabulate
from datetime import datetime

# ==============================
# CONFIG
# ==============================
FILE_NAME = "expenses.csv"
COLUMNS = ["Date", "Amount", "Category", "Description"]

# ==============================
# INITIAL SETUP
# ==============================
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=COLUMNS)
    df.to_csv(FILE_NAME, index=False)

# ==============================
# CORE FUNCTIONS
# ==============================
def load_data():
    try:
        df = pd.read_csv(FILE_NAME)
        if df.empty:
            return pd.DataFrame(columns=COLUMNS)
        return df
    except Exception:
        return pd.DataFrame(columns=COLUMNS)

def save_data(df):
    df.to_csv(FILE_NAME, index=False)

def add_expense():
    try:
        amount = float(input("💵 Enter amount: "))
        if amount <= 0:
            print("❌ Amount must be positive!\n")
            return

        category = input("📂 Enter category (Food, Travel, Bills, etc.): ").title()
        description = input("📝 Enter description: ")
        date = datetime.now().strftime("%Y-%m-%d")

        df = load_data()
        new_expense = pd.DataFrame([[date, amount, category, description]], columns=COLUMNS)
        df = pd.concat([df, new_expense], ignore_index=True)
        save_data(df)

        print("\n✅ Expense added successfully!\n")
    except ValueError:
        print("\n❌ Invalid input! Please enter a valid number.\n")

def view_expenses():
    df = load_data()
    if df.empty:
        print("\n📂 No expenses found!\n")
    else:
        print("\n📜 All Expenses:\n")
        print(tabulate(df, headers="keys", tablefmt="pretty"))

def monthly_summary():
    df = load_data()
    if df.empty:
        print("\n📂 No expenses found!\n")
        return

    current_month = datetime.now().strftime("%Y-%m")
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_df = df[df['Date'].dt.strftime('%Y-%m') == current_month]

    if monthly_df.empty:
        print(f"\n📅 No expenses found for {current_month}\n")
        return

    total = monthly_df['Amount'].sum()
    avg = monthly_df['Amount'].mean()
    max_exp = monthly_df.loc[monthly_df['Amount'].idxmax()]

    print(f"\n📅 Monthly Summary ({current_month}):")
    print(f"💰 Total Spent: {total}")
    print(f"📊 Average Expense: {avg:.2f}")
    print(f"🔝 Biggest Expense: {max_exp['Amount']} ({max_exp['Category']} - {max_exp['Description']})\n")

def category_summary():
    df = load_data()
    if df.empty:
        print("\n📂 No expenses found!\n")
        return

    current_month = datetime.now().strftime("%Y-%m")
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_df = df[df['Date'].dt.strftime('%Y-%m') == current_month]

    if monthly_df.empty:
        print(f"\n📂 No category expenses for {current_month}\n")
        return

    category_group = monthly_df.groupby("Category")["Amount"].sum().reset_index()
    print(f"\n📊 Category-wise Breakdown ({current_month}):\n")
    print(tabulate(category_group, headers="keys", tablefmt="pretty"))

def search_expenses():
    df = load_data()
    if df.empty:
        print("\n📂 No expenses found!\n")
        return

    keyword = input("🔍 Enter category/description keyword to search: ").strip().lower()
    result = df[df.apply(lambda row: keyword in str(row['Category']).lower() 
                         or keyword in str(row['Description']).lower(), axis=1)]

    if result.empty:
        print("\n❌ No matching records found!\n")
    else:
        print("\n🔍 Search Results:\n")
        print(tabulate(result, headers="keys", tablefmt="pretty"))

# ==============================
# MAIN MENU
# ==============================
def main():
    while True:
        print("\n===== 💼 Expense Tracker =====")
        print("1️⃣ Add Expense")
        print("2️⃣ View All Expenses")
        print("3️⃣ Monthly Summary")
        print("4️⃣ Category-wise Breakdown")
        print("5️⃣ Search Expenses")
        print("6️⃣ Exit")

        choice = input("\n👉 Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            search_expenses()
        elif choice == "6":
            print("\n👋 Exiting... Stay financially sharp!\n")
            break
        else:
            print("\n❌ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
