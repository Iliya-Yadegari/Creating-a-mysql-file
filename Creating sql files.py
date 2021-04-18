from tkinter import *
import mysql.connector as msc

def create_fun():
    mydb = msc.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'myfirstdatabase'
        )

    mycursor = mydb.cursor()
    mycursor.execute('SHOW DATABASES')

    for db in mycursor:
        if db == dataBase_ent.get():
            messagebox.showinfo('Result','This file already exists')

        else:
            mycursor.execute(f'CREATE DATABASE {dataBase_ent.get()}')
            messagebox.showinfo('Result','Your file has been successfully created')


window = Tk()

window.title('Creating databases')

main_frm = LabelFrame(window,text = 'Creating Database').grid(row = 0, column = 0, padx = 10, pady = 10)

dataBase_lbl = Label(main_frm,text = 'Enter the name of the database you want to create ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
dataBase_ent = Entry(main_frm)
submit_btn = Button(main_frm,text = 'Submit',width = 20, height = 3,command = create_fun).grid(row = 1, column = 0, padx = 10, pady = 10)

dataBase_ent.grid(row = 0, column = 1, padx = 10, pady = 10)

window.mainloop()