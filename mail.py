import smtplib as s
from tkinter import *
def sending():

    add_info = add.get()

    body_info = body.get()


    sender_email = "pavelnarayan660@gmail.com" 

    sender_password = "twopy.2020"

    serv = s.SMTP('smtp.gmail.com',587)

    serv.starttls()

    serv.login(sender_email,sender_password)

    print("Successfully logged in")

    serv.sendmail(sender_email,add_info,body_info)

    print("Message sent and recieved by user")
    add_entry.delete(0,END)
    body_entry.delete(0,END)



def whole():
    app = Tk()
    app.title('Mail')
    app.geometry("500x500")

    add_field = Label(app,text="Email address :")
    body_field = Label(app,text="Message :")

    add_field.place(x=15,y=70)
    body_field.place(x=15,y=140)
    global add
    global body
    add = StringVar()
    body = StringVar()
    global add_entry
    global body_entry

    add_entry = Entry(textvariable=add,width="30")
    body_entry = Entry(textvariable=body,width="30")

    add_entry.place(x=15,y=100)
    body_entry.place(x=15,y=180)

    button = Button(app,text="Click to send message",command=sending ,width="30",height="2",bg="white")

    button.place(x=15,y=220)


    mainloop()
