import pickle
from colorama import Fore, Back, Style
import dateparser
from manager import FinancialManager

print(Fore.GREEN + """
     /$$      /$$                                               /$$$$$$$$                           /$$                          
    | $$$    /$$$                                              |__  $$__/                          | $$                          
    | $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$         | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
    | $$ $$/$$ $$ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$         | $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
    | $$  $$$| $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  | $$         | $$| $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
    | $$\  $ | $$| $$  | $$| $$  | $$| $$_____/| $$  | $$         | $$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$      
    | $$ \/  | $$|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$         | $$| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
    |__/     |__/ \______/ |__/  |__/ \_______/ \____  $$         |__/|__/      \_______/ \_______/|__/  \__/ \_______/|__/      
                                                /$$  | $$                                                                        
                                               |  $$$$$$/                                                                        
                                                \______/                                                                         
""" + Style.RESET_ALL)

print("""
    Please, choose one of the options:

    [0]. Show all account information
    [1]. Add income
    [2]. Add expense
    [3]. Quit

""")

finc_manager = FinancialManager()

balance = 0
income_categories = {
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

income_history = []

try:
    with open("history_file.pkl", "rb") as file:
        income_history = pickle.load(file)
except EOFError:
    income_history = {}
except FileNotFoundError:
    print(Fore.RED + "File 'contacts.pkl' not found. Creating a new income list." + Style.RESET_ALL)
    income_history = {}

while True:
    option = int(input("Option: "))

    if option == 1:
        category_num = int(input(Fore.YELLOW + """
                          _CHOOSE A CATEGORY_

        [1]. Salary                     [6]. Business Income
        [2]. Freelance Income           [7]. Interest and Dividends
        [3]. Rental Income              [8]. Gifts and Bonuses
        [4]. Investment Income          [9]. Alimony or Child Support
        [5]. Side Gig Income            [10]. Miscellaneous Income

        Only number: """ + Style.RESET_ALL))

        # Проверяем, что введенное число находится в диапазоне от 1 до 10
        if category_num < 1 or category_num > 10:
            print(Fore.RED + "Wrong category number!" + Style.RESET_ALL)
            continue

        category = income_categories[category_num]
        income = input("\nInput amount: ") + " soms"
        date = input("Input a date as you want: ")
        formatted_date = dateparser.parse(date)

        record = {
            "Category": category,
            "Income": income,
            "Date": formatted_date.strftime("%d/%m/%Y") if formatted_date else None
        }

        income_history.append(record)

        with open("history_file.pkl", "wb") as file:
            pickle.dump(income_history, file)

        print(Fore.MAGENTA + "Data has been saved!\n" + Style.RESET_ALL)



