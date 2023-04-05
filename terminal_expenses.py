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

def total():
    """ This function reads the expenses.txt file and converts each line into a float, adding them to a expenses list. The total invoice amount is obtained by summing the list """
    with open('data/expenses.txt', 'r') as f:
        expenses = [float(line.strip()) for line in f]
        total = sum(expenses)
        print(f"Total invoice amount: ${total}")

def show():
    """ This function just prints each line of the expenses.txt without whitespace between them """
    with open('data/expenses.txt', 'r') as f:
        for line in f:
            print(line.strip())

def reset():
    """ This function deletes the data from expenses.txt """
    with open('data/expenses.txt', 'w') as f:
        f.write("")

def set_ceiling():
    """ This function sets the ceiling - the ideal expenses cap the user wants in the month """
    with open('data/ceiling.txt', 'w') as f:
        new_ceiling = input("New ceiling: ")
        f.write("")
        f.write(new_ceiling)

def ceiling():
    """ This function shows the ceiling and the remaining money left from it """
    with open('data/ceiling.txt', 'r') as c:
        ceiling_list = [float(line) for line in c]
        ceiling = sum(ceiling_list)
    with open('data/expenses.txt', 'r') as f:
        expenses = [float(line.strip()) for line in f]
        total = sum(expenses)
    remaining = ceiling - total
    print(f"Ceiling: ${ceiling} \nMoney spent: ${total} \nMoney left: ${remaining}")
