from pynput.keyboard import Key, Controller
import main
import time
import pyautogui 
def launch(query):
    if 'launch' in query:
        query = query.replace("launch", "")
    elif 'open' in query:
        query = query.replace("open", "")
    keyboard = Controller()


    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)

    time.sleep(1)


    for char in query:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.11)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)

    if 'skype' in query:
        main.Goverbal('what would you like to do?')
        options=main.Input()
        if 'video' in options:
            main.Goverbal('who would you like to call?')
            name=main.Input()
            pyautogui.moveTo(201, 152, duration = 0.5)  #158,318
            pyautogui.click(201,152)
            pyautogui.moveTo(185, 101, duration = 0.5)  #158,318
            pyautogui.click(185,101)
            time.sleep(5)
            pyautogui.typewrite(name)
            time.sleep(4)
            pyautogui.moveTo(158, 318, duration = 0.5)  #158,318
            pyautogui.click(158,318)
            pyautogui.moveTo(1144, 80, duration = 0.5)  #158,318
            pyautogui.click(1144,80)
        elif 'voice' in options:
            main.Goverbal('who would you like to call?')
            name=main.Input()
            pyautogui.moveTo(201, 152, duration = 0.5)  #158,318
            pyautogui.click(201,152)
            pyautogui.moveTo(185, 101, duration = 0.5)  #158,318
            pyautogui.click(185,101)
            time.sleep(5)
            pyautogui.typewrite(name)
            time.sleep(4)
            pyautogui.moveTo(158, 318, duration = 0.5)  #158,318
            pyautogui.click(158,318)
            pyautogui.moveTo(1282, 74, duration = 0.5)  #158,318
            pyautogui.click(1282,74)

    if 'chrome' in query:
        main.Goverbal('What would you like to do?')
        option=Input()
        if option == 'search':
            main.Goverbal('enter your search')
            query=main.Input()
            pyautogui.typewrite(query)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif option=='history':
             pyautogui.hotkey("ctrlleft", "h")
            

        
        elif option == 'private':
            pyautogui.typewrite(["ctrlleft","shift","n"])
