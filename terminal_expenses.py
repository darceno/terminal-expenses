def add():
    """ This function asks for a value and, if it's a number, adds it to the expenses.txt file """
    with open('data/expenses.txt', 'a') as f:
        new_expense = input("New expense: ")
        while new_expense != "0":
            if new_expense.isdigit():
                f.write(new_expense + "\n")
                new_expense = input("New expense: ")
            else:
                print("Enter a valid valor")
                new_expense = input("New expense: ")