from colorama import Fore, Style
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

from colorama import Fore, Style

print(f"""
    Please, choose one of the options:

    [{Fore.GREEN}0{Style.RESET_ALL}]. Show all account information
    [{Fore.GREEN}1{Style.RESET_ALL}]. Add income
    [{Fore.GREEN}2{Style.RESET_ALL}]. Add expense
    [{Fore.GREEN}3{Style.RESET_ALL}]. Display balance
    [{Fore.GREEN}4{Style.RESET_ALL}]. Quit

""")

dp = FinancialManager()
dp.load_income_history()
dp.load_expense_history()

while True:
    option = int(input("Option: "))

    if option == 0:
        dp.display_information()

    if option == 1:
        category_num = int(input(Fore.YELLOW + """
                          _CHOOSE A CATEGORY_
        
        [1]. Salary                     [6]. Business Income
        [2]. Freelance Income           [7]. Interest and Dividends
        [3]. Rental Income              [8]. Gifts and Bonuses
        [4]. Investment Income          [9]. Alimony or Child Support
        [5]. Side Gig Income            [10]. Miscellaneous Income
        
        Only number: """ + Style.RESET_ALL))


        income = int(input("\nInput amount: "))
        date = input("Input a date as you want: ")

        dp.add_income(category_num, income, date)
        dp.save_income_history()
        dp.save_balance()

        print(Fore.MAGENTA + "Data has been saved!\n" + Style.RESET_ALL)

    if option == 2:
        category_num = int(input(Fore.YELLOW + """
                                  _CHOOSE A CATEGORY_

                [1]. Housing                     [6]. Debt Payments
                [2]. Transportation              [7]. Entertainment
                [3]. Food                        [8]. Education
                [4]. Utilities                   [9]. Savings
                [5]. Healthcare                  [10]. Other

                Only number: """ + Style.RESET_ALL))

        expense = int(input("\nInput amount: ")) * -1
        date = input("Input a date as you want: ")

        dp.add_expense(category_num, expense, date)
        dp.save_expense_history()
        dp.save_balance()

        print(Fore.MAGENTA + "Data has been saved!\n" + Style.RESET_ALL)

    if option == 3:
        print(f"Balance: {dp.get_balance()}")

    if option == 4:
        print("See you again!")
        break



