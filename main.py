import pyttsx3 
import speech_recognition   
import datetime
import wikipedia 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import clock
import whatsapp
import Wiki
import contact
import srch
import shutdown
import alarm
import launch
import password
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def Goverbal(audio): 
    engine.say(audio)
    engine.runAndWait()
    

def Greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Goverbal("Good Morning!")

    elif hour>=12 and hour<18:
        Goverbal("Good Afternoon!")   

    else:
        Goverbal("Good Evening!")  

    Goverbal("I am TWO PY .")       

def Input():

    global query
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        Goverbal("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 350
        audio = r.listen(source)

    try:
        Goverbal("Recognizing...")    
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)    
        Goverbal("Sorry i didn't quite catch that. Say it again")  
        Input()
     
    return query

if __name__ == "__main__":
    Greet()
    while True:
    # if 1:
        query = Input().lower()
        if 'bye' in query:
            break
        l=['wikipedia','whatsapp','the time','contact','alarm','shutdown','password','launch','open']
        if 'contact' in query:
            contact.con()
        if 'wikipedia' in query:
            Wiki.wiki(query)
        if 'whatsapp' in query:
            whatsapp.whatsapp()
        if 'the time' in query:
            clock.time()
        if 'alarm' in query:
            alarm.alarm() 
        
        if 'shutdown' in query:
            shutdown.off()
        if 'password' in query:
            password.key()
        
        
        c=0
        for i in l:
            if i in query:
                c=c+1
            
        print(c)    
        if c == 0:
            srch.srch(query)  
            
                

      
           
            


        