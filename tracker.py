import sqlite3
import matplotlib.pyplot as plt
from tabulate import tabulate


def add_expense(amount, category, note, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, note, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, note, date))

    conn.commit()
    conn.close()

    print("Expense added successfully!")


def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    headers = ["ID", "Amount", "Category", "Note", "Date"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))


def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()
    conn.close()

    print("Expense deleted successfully!")


def update_expense(expense_id, amount, category, note, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, note = ?, date = ?
        WHERE id = ?
    """, (amount, category, note, date, expense_id))

    conn.commit()
    conn.close()

    print("Expense updated successfully!")


def total_expense():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()

    print("Total Expense:", total)


def category_expense():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    rows = cursor.fetchall()
    conn.close()

    print("\nCategory-wise Expense:")
    for row in rows:
        print(row[0], ":", row[1])


def category_pie_chart():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    data = cursor.fetchall()
    conn.close()

    if not data:
        print("No data to display chart!")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Category-wise Expense Distribution")
    plt.show()