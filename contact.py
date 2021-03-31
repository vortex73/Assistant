import mysql.connector

import tkinter as tk 


def con():
    def submit(): 
        root=tk.Tk() 

        root.title('Contact')
        root.geometry("600x400") 


        name_var=tk.StringVar() 
        email_var=tk.StringVar() 
        phone_var=tk.StringVar()
        a=mysql.connector.connect(host="localhost",port='3306',user="root",passwd="1234",database="assistant")

        global ab
        global emailid
        global phone
        ab=name_var.get()   
        emailid=email_var.get() 
        phone=phone_var.get()

        cursor=a.cursor()
        b="Insert into contacts (Name,Phone,Email) values "+str((ab,phone,emailid))
        cursor.execute(b)
        a.commit()
        a.close()



        name_var.set("") 
        email_var.set("") 
        phone_var.set("")


    name_label = Label(root, text = 'Name', 
    font=('calibre',10, 'bold')) 

    name_entry = Entry(root, 
    textvariable = name_var,
    font=('calibre',10,'normal')) 


    emailid_label = Label(root, 
    text = 'mail-id', 
    font = ('calibre',10,'bold')) 


    emailid_entry=Entry(root, 
    textvariable = email_var, 
    font = ('calibre',10,'normal')) 

    phone_label = Label(root, 
    text = 'phone number', 
    font = ('calibre',10,'bold')) 


    phone_entry=Entry(root, 
    textvariable = phone_var, 
    font = ('calibre',10,'normal')) 					

    sub_btn=Button(root,text = 'Submit', 
    command = submit) 

    name_label.grid(row=0,column=0) 
    name_entry.grid(row=0,column=1) 
    emailid_label.grid(row=1,column=0) 
    emailid_entry.grid(row=1,column=1)
    phone_label.grid(row=2,column=0) 
    phone_entry.grid(row=2,column=1)  
    sub_btn.grid(row=3,column=1) 
    root.mainloop()
