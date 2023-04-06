def add():
    """ This function asks for a value and, if it's a number, adds it to the expenses.txt file """
    with open('data/expenses.txt', 'a') as f:
        new_expense = input("New expense (type 0 when finished): ")
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
    """ This function print each line of the expenses.txt without whitespace between them """
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

def help():
    """ This function prints a short description of the program, as well as a list of possible commands """
    print("Hello! This is a very basic program to calculate expenses\n \n\033[1mList of commands: \033[0m\nadd — for storing a new expense \nshow — for displaying a list of of every expense \ntotal - for displaying the total value of every summed expense \nreset — for reseting the list of expenses to $0 \nset ceiling — for setting a new ceiling value, the maximum money you can spend \nceiling — for showing how much money you still have avaliable, based on the ceiling value \nhelp — for reading this again")