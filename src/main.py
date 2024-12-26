import tkinter
import sqlite3


def init():
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()
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
    return connection, cursor


def main():
    connection, cursor = init()
    root = tkinter.Tk()
    root.title('PESOurce')
    root.geometry('1000x700')
    root.mainloop()

if __name__ == '__main__':
    main()
