import main
import datetime
def time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    main.Goverbal(f" the time is {strTime}")