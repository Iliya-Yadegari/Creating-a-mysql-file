from tkinter import *
import CreatingSqlModule as csm
            


window = Tk()

window.title('Creating databases')
window.iconbitmap('document.ico')

main_frm = LabelFrame(window,text = 'Creating Database').grid(row = 0, column = 0, padx = 10, pady = 10)

dataBase_lbl = Label(main_frm,text = 'Enter the name of the database you want to create ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
dataBase_ent = Entry(main_frm)
submit_btn = Button(main_frm,text = 'Submit',width = 20, height = 3,command = lambda: csm.create_fun(dataBase_ent.get())).grid(row = 1, column = 0, padx = 10, pady = 10)

dataBase_ent.grid(row = 0, column = 1, padx = 10, pady = 10)

window.mainloop()