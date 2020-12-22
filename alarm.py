import pygame
import time
import main
def alarm():
   main.Goverbal("Enter the hour")
   hr=int(main.Input())
   main.Goverbal("Enter the minute")
   mn=int(main.Input())
   pygame.mixer.init()
   sound = pygame.mixer.Sound("bullet.mp3")

   n=5  

   print("Alarm set for",str(hr),":",str(mn))
   while True:
       if time.localtime().tm_hour==hr and time.localtime().tm_min==mn :
           print("Wake up") 
           break
    
        
   while n>0:
       sound.play()
       time.sleep(2)

   snz=main.Input()
   if snz=='Stop':
       n=3
       time.sleep(100)
       while n>0:
           sound.play()
           time.sleep(2)
   else:
       exit()
       sound()
       alarm()