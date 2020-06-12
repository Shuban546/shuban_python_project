from tkinter import*
import mysql.connector
import random
from tkinter import messagebox
my_database = mysql.connector.connect(user='root', password='shuban1234$',host='localhost', database='mysql',auth_plugin='mysql_native_password')
cursor=my_database.cursor()

def newfile():
     root=Tk()
     root.title("LIBRARY SYSTEMS")
     welcome_label=Label(root,text="NAME").grid(row=0,column=0)

def welcome(name):
   
     root=Tk()
     root.title("LIBRARY SYSTEMS")
     root.geometry("500x500")

     welcome_label=Label(root,text="WELCOME "+name).pack()

     menu = Menu(root)
     root.config(menu=menu)
     filemenu = Menu(menu) 
     menu.add_cascade(label='USER', menu=filemenu) 
     filemenu.add_command(label='PROFILE',command=newfile) 
     #filemenu.add_command(label='Open...') 
     #filemenu.add_command(label='Exit', command=root.quit) 
     #helpmenu = Menu(menu) 
     filemenu.add_command(label='SETTINGS') 
     filemenu.add_command(label='BORROW BOOKS')
     filemenu.add_command(label='RETURN BOOKS')


def error():
     messagebox.showinfo("ERROR","PLEASE ENTER VALID NAME OR PASSWORD")

def register():
     
     my_database = mysql.connector.connect(user='root', password='shuban1234$',host='localhost', database='mysql',auth_plugin='mysql_native_password')

     cursor=my_database.cursor()
     name=name_var.get()
     password=password_var.get()
  
     name_var.set("")
     password_var.set("")

     if name=="" or password=="":
         error()
              
     else:
         welcome(name)#writen in welcome.py
         
     root.destroy()
        
root=Tk()
root.title("LIBRARY MANAGEMENT SYSTEMS")
root.geometry("500x500")

name_var=StringVar()
password_var=StringVar()
studentid_var=StringVar()

enter_label=Label(root,text="ENTER THE DETAILS*",width=20,height=1).pack()
blank_label=Label(root,text="").pack()

name_label=Label(root,text="NAME*",height=2).pack()
name_entry=Entry(root,textvariable=name_var).pack()

password_label=Label(root,text="PASSWORD*",height=2).pack()
password_entry=Entry(root,textvariable=password_var,show="*").pack()

blank_label=Label(root,text="").pack()

submit_button=Button(root,text="REGISTER",command=register).pack()

name=name_var.get()
password=password_var.get()

