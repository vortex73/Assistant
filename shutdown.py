import os
import main
def off():
    
    main.Goverbal("Do you wish to shutdown your computer ? ")
    shutdown = main.Input() 
  
    if shutdown == 'no': 
        exit() 
    else: 
        main.Goverbal('ok bye')
        os.system("shutdown /s /t 1")