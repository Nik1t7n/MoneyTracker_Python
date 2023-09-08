import pickle
import dateparser
from colorama import Fore, Style
import sqlite3

class FinancialManager:
    def __init__(self):
        self.balance = 0

        self.income_categories = {
            1: "Salary",
            2: "Freelance Income",
            3: "Rental Income",
            4: "Investment Income",
            5: "Side Gig Income",
            6: "Business Income",
            7: "Interest and Dividends",
            8: "Gifts and Bonuses",
            9: "Alimony or Child Support",
            10: "Miscellaneous Income"
        }
        self.income_history = []

        self.expense_categories = {
            1: "Housing",
            2: "Transportation",
            3: "Food",
            4: "Utilities",
            5: "Healthcare",
            6: "Debt Payments",
            7: "Entertainment",
            8: "Education",
            9: "Savings",
            10: "Miscellaneous"
        }
        self.expense_history = []

        self.db = sqlite3.connect("database.db")
        self.sql = self.db.cursor()

    def load_income_history(self):
        try:
            self.sql.execute("SELECT category, income, date FROM income_history")
            rows = self.sql.fetchall()

            for row in rows:
                category, income, date = row
                record = {
                    "Category": category,
                    "Income": income,
                    "Date": date
                }
                self.income_history.append(record)

        except sqlite3.Error as e:
            print(Fore.RED + "SQLite error:", e, Style.RESET_ALL)

    def save_income_history(self):
        try:
            for record in self.income_history:
                category = record["Category"]
                income = record["Income"]
                date = record["Date"]

                self.sql.execute("INSERT INTO income_history (category, income, date) VALUES (?,?,?)", (category, income, date))
                self.db.commit()

        except sqlite3.Error as e:
            print(Fore.RED + "SQLite error:", e, Style.RESET_ALL)

    def add_income(self, category_num, income, date):
        if category_num < 1 or category_num > 10:
            print(Fore.RED + "Wrong category number!" + Style.RESET_ALL)

        category = self.income_categories[category_num]
        formatted_date = dateparser.parse(date)
        formatted_date_str = formatted_date.strftime("%d/%m/%Y") if formatted_date else None

        record = {
            "Category": category,
            "Income": income,
            "Date": formatted_date_str
        }

        self.balance += int(income)
        self.income_history.append(record)

    def get_balance(self):
        try:
            self.sql.execute("SELECT balance FROM balance")
            balance_all = self.sql.fetchall()

            if balance_all:
                return balance_all[-1][0]
            else:
                return 0


        except sqlite3.Error as e:
            print(Fore.RED + "SQLite error:", e, Style.RESET_ALL)

    def add_expense(self, category_num, expense, date):
        if category_num < 1 or category_num > 10:
            print(Fore.RED + "Wrong category number!" + Style.RESET_ALL)

        category = self.expense_categories[category_num]
        formatted_date = dateparser.parse(date)
        formatted_date_str = formatted_date.strftime("%d/%m/%Y") if formatted_date else None

        record = {
            "Category": category,
            "Expense": expense,
            "Date": formatted_date_str
        }

        self.balance += int(expense)
        self.expense_history.append(record)

    def load_expense_history(self):
        try:
            self.sql.execute("SELECT category, expense, date FROM expense_history")
            rows = self.sql.fetchall()

            for row in rows:
                category, expense, date = row
                record = {
                    "Category": category,
                    "Expense": expense,
                    "Date": date
                }
                self.expense_history.append(record)

        except sqlite3.Error as e:
            print(Fore.RED + "SQLite error:", e, Style.RESET_ALL)

    def save_expense_history(self):
        try:
            for record in self.expense_history:
                category = record["Category"]
                expense = record["Expense"]
                date = record["Date"]

                self.sql.execute("INSERT INTO expense_history (category, expense, date) VALUES (?,?,?)",
                                 (category, expense, date))
                self.db.commit()

        except sqlite3.Error as e:
            print(Fore.RED + "SQLite error:", e, Style.RESET_ALL)

    def save_balance(self):
        try:
            balnc = int(self.balance)
            self.sql.execute("INSERT INTO balance (balance) VALUES (?)", (balnc,))
            self.db.commit()


        except sqlite3.Error as e:
            print(Fore.RED + "SQLite error:", e, Style.RESET_ALL)

    def display_information(self):

        balance_print = self.get_balance()
        print(f"Balance: {balance_print}")

        print("Incomes: \n")
        for record in self.income_history:
            category = record["Category"]
            income = record["Income"]
            date = record["Date"]
            print(f"""
            Category: {category}
            Amount: {income}
            Date: {date}

            """)

        print("Expenses: \n")
        for record in self.expense_history:
            category = record["Category"]
            expense = record["Expense"]
            date = record["Date"]
            print(f"""
            Category: {category}
            Amount: {expense}
            Date: {date}

            """)

