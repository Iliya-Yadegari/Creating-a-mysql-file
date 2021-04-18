from tkinter import *





window = Tk()

dataBase_lbl = Label(window,text = 'Enter the name of the database you want to create ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
dataBase_ent = Entry(window).grid(row = 0, column = 1, padx = 10, pady = 10)
submit_btn = Button(window,text = 'Submit',width = 20, height = 3).grid(row = 1, column = 0, padx = 10, pady = 10)


window.mainloop()