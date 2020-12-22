import smtplib as s
import tkinter as tk
global root

root=tk.Tk() 

root.geometry("600x400") 

sub_var=tk.StringVar() 
bod_var=tk.StringVar()
mail_var=tk.StringVar()
def submit():
    global sa
    global b
    global m


    sa=sub_var.get()
    b=bod_var.get()
    m=mail_var.get()

    sub_var.set("")
    bod_var.set("")
    mail_var.set("")

sub_label = tk.Label(root, text = 'Subject', font=('calibre',10, 'bold')) 

sub_entry = tk.Entry(root, textvariable = sub_var, font=('calibre',10,'normal'))


bod_label = tk.Label(root, text = 'Body', font = ('calibre',10,'bold')) 


bod_entry = tk.Entry(root, textvariable = bod_var, font = ('calibre',10,'normal')) 

mail_label = tk.Label(root, text = 'Email-id', font = ('calibre',10,'bold')) 


mail_entry=tk.Entry(root, textvariable = mail_var, font = ('calibre',10,'normal')) 


send_btn=tk.Button(root,text = 'Send', command= submit) 

sub_label.grid(row=0,column=0) 
sub_entry.grid(row=0,column=1) 
bod_label.grid(row=1,column=0) 
bod_entry.grid(row=1,column=1)
mail_label.grid(row=2,column=0) 
mail_entry.grid(row=2,column=1) 
send_btn.grid(row=3,column=1) 
root.mainloop()



ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("pavelnarayan660@gmail.com","twopy.2020")


message="Subject:{}\n\n{}".format(sa,b)




ob.sendmail("pavelnarayan660@gmail.com", m ,message)
print('Sent Successfully')
ob.quit()
