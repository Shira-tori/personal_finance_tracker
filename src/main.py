import tkinter
import sqlite3

def main():
    connection = sqlite3.connect('data/data.db')
    root = tkinter.Tk()
    root.title('PESOurce')
    root.geometry('1000x700')
    root.mainloop()

if __name__ == '__main__':
    main()
