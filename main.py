<<<<<<< HEAD
from tracker import view_expenses, total_expense, category_expense, category_pie_chart

print("\n--- EXPENSE TRACKER DASHBOARD ---\n")

view_expenses()
total_expense()
category_expense()
category_pie_chart()
=======
# main.py
# REST API Data Fetcher & Dashboard

from api_handler import fetch_data
from tabulate import tabulate
import matplotlib.pyplot as plt

# Example Public API
API_URL = "https://jsonplaceholder.typicode.com/posts"


def display_table(data):
    """
    Display API data in table format
    """

    table_data = []

    for item in data[:10]:  # limit output
        table_data.append([item["id"], item["title"][:50]])

    headers = ["Post ID", "Post Title"]

    print(tabulate(table_data, headers=headers, tablefmt="grid"))


def plot_chart(data):
    """
    Create bar chart for posts per user
    """

    user_counts = {}

    for item in data:
        user_id = item["userId"]
        user_counts[user_id] = user_counts.get(user_id, 0) + 1

    plt.bar(user_counts.keys(), user_counts.values())

    plt.title("Posts per User ID")
    plt.xlabel("User ID")
    plt.ylabel("Number of Posts")

    # Save chart for submission
    plt.savefig("screenshots/chart.png")

    plt.show()


def main():

    # ⭐ Project Header
    print("=" * 50)
    print("     REST API DATA FETCHER & DASHBOARD")
    print("=" * 50)

    print("\n🚀 Starting project...\n")

    # Fetch data
    data = fetch_data(API_URL)

    if data:
        print("\n📋 TABLE VIEW:\n")
        display_table(data)

        print("\n📊 OPENING CHART...\n")
        plot_chart(data)

    else:
        print("❌ No data received from API")


if __name__ == "__main__":
    main()
>>>>>>> 13d0321e0722683eba2d406fb95cce595225aa26
