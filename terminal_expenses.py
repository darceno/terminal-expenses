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
    """ This function reads the expenses.txt file and converts each line into a float, adding them to a expenses list. The total invoice amount is obtained by summing the list"""
    with open('data/expenses.txt', 'r') as f:
        expenses = [float(line.strip()) for line in f]
        total = sum(expenses)
        print(f"Total invoice amount: ${total}")
