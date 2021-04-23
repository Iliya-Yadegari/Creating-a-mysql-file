import mysql.connector as msc
from tkinter import *

def create_fun(dataBase_e):
    mydb = msc.connect(
        host = 'localhost',
        user = 'root',
        password = ''
        )

    mycursor = mydb.cursor()
    mycursor.execute('SHOW DATABASES')

    

    for db in mycursor:
        data = list(dataBase_e)
        joined_data = "".join(data)
        
        db = list(db)
        joined_db = "".join(db)
        
        if joined_db == joined_data:

            messagebox.showinfo('Result','This file already exists')
            return  


        
    mycursor.execute(f'CREATE DATABASE {dataBase_e}')
    messagebox.showinfo('Result','Your file has been successfully created')