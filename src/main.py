import tkinter
import sqlite3
import input

class PESOurce():
    connection = None
    cursor = None
    def __init__(self):
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
        connection = connection
        cursor = cursor

    def main(self):
        print("************************")
        print("* Welcome to PESOurce. *")
        print("************************\n")
        print('1. Add Income')
        print('2. Add Expense')
        print('3. View Summary')
        print('4. Visualize Spending\n')
        choice = input.get_input()

if __name__ == '__main__':
    program = PESOurce()
    program.main()
