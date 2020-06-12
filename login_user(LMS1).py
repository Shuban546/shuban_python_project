from tkinter import*
import mysql.connector



def login():
    id_user=id_var.get()
    password=password_var.get()

    my_database = mysql.connector.connect(user='root', password='shuban1234$',
                              host='localhost', database='mysql',
                              auth_plugin='mysql_native_password')

    cursor=my_database.cursor()

    cursor.execute('use library')
    
    entry=cursor.execute('select password from user where name = "shuban";')

    
    print(entry)

   
    
    password_var.set("")
    id_var.set("")

root=Tk()
root.title("LIBRARY MANAGEMENT SYSTEMS")
root.geometry("500x500")

id_var=StringVar()
password_var=StringVar()

enter_label=Label(root,text="ENTER THE DETAILS*",width=20,height=1).pack()
blank_label=Label(root,text="").pack()

id_label=Label(root,text="ID*",height=2).pack()
id_entry=Entry(root,textvariable=id_var).pack()

password_label=Label(root,text="PASSWORD*",height=2).pack()
password_entry=Entry(root,textvariable=password_var,show="*").pack()

blank_label=Label(root,text="").pack()

submit_button=Button(root,text="LOGIN",command=login).pack()
