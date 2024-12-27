import tkinter
import sqlite3
import input


def init():
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            CREATE TABLE finance_tracker(
                type text,
                ammount text,
                category text,
                date text
            ) 
            """
        )
        connection.commit()
    except:
        pass
    return connection, cursor


def main():
    connection, cursor = init()
    print("************************")
    print("* Welcome to PESOurce. *")
    print("************************\n")
    print('1. Add Income')
    print('2. Add Expense')
    print('3. View Summary')
    print('4. Visualize Spending\n')
    input.getInput()

if __name__ == '__main__':
    main()
