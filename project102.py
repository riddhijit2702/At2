import pyautogui
import time


start_time = time.time()


def main():
    while(True):
        if((time.time() - start_time) >= 60*60):  
            print(start_time)
            pyautogui.alert("Take a break")

main()    