import mysql.connector

import tkinter as tk 
global root
root=tk.Tk() 


root.geometry("600x400") 


name_var=tk.StringVar() 
email_var=tk.StringVar() 
phone_var=tk.StringVar()

def submit(): 
    a=mysql.connector.connect(host="localhost",port='3306',user="root",passwd="root123",database="pavel")

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


name_label = tk.Label(root, text = 'Name', 
font=('calibre',10, 'bold')) 

name_entry = tk.Entry(root, 
textvariable = name_var,
font=('calibre',10,'normal')) 


emailid_label = tk.Label(root, 
text = 'mail-id', 
font = ('calibre',10,'bold')) 


emailid_entry=tk.Entry(root, 
textvariable = email_var, 
font = ('calibre',10,'normal')) 

phone_label = tk.Label(root, 
text = 'phone number', 
font = ('calibre',10,'bold')) 


phone_entry=tk.Entry(root, 
textvariable = phone_var, 
font = ('calibre',10,'normal')) 					

sub_btn=tk.Button(root,text = 'Submit', 
command = submit) 

name_label.grid(row=0,column=0) 
name_entry.grid(row=0,column=1) 
emailid_label.grid(row=1,column=0) 
emailid_entry.grid(row=1,column=1)
phone_label.grid(row=2,column=0) 
phone_entry.grid(row=2,column=1)  
sub_btn.grid(row=3,column=1) 
root.mainloop()




root.geometry("600x400") 

ex_var=tk.StringVar() 

def extract():
    a=mysql.connector.connect(host="localhost",port='3306',user="root",passwd="root123",database="pavel")
    
    global ext
    global data
    
    ext=ex_var.get()
    
    cursor=a.cursor()
    b="SELECT Phone, Email from contacts WHERE Name = ext "
    cursor.execute(b)
    data=cursor.fetchall()
    print(data)

    a.close()

    ex_var.set("")

ex_label = tk.Label(root, text = 'Name', font=('calibre',10, 'bold')) 

ex_entry = tk.Entry(root, textvariable = ex_var, font=('calibre',10,'normal')) 

sear_btn = tk.Button(root,text = 'Search', command = extract) 

ex_label.grid(row=0,column=0) 
ex_entry.grid(row=0,column=1)
sear_btn.grid(row=1,column=1) 
root.mainloop()

print("The Phone number is" , data[0])
print("The Email-id is" , data[1])
