"""
    Bulk sender script. Use to write large number of messages and send them by auto pressing enter. 
"""
from pyautogui import write, press
from time import sleep
from os import system


def logo():
    print("""\033[38;5;201m
 ______                                             _                    _                   
|  ___ \                                           | |                  | |                  
| | _ | |  ____   ___   ___   ____   ____   ____   | | _    ___   ____  | | _    ____   ____ 
| || || | / _  ) /___) /___) / _  | / _  | / _  )  | || \  / _ \ |    \ | || \  / _  ) / ___)
| || || |( (/ / |___ ||___ |( ( | |( ( | |( (/ /   | |_) )| |_| || | | || |_) )( (/ / | |    
|_||_||_| \____)(___/ (___/  \_||_| \_|| | \____)  |____/  \___/ |_|_|_||____/  \____)|_|    
                                   (_____|                                                   
          """)


def addSubStringAfterIndex(originalString, index, substring):
    """This function will add passed substring after given index of the string"""
    newString = originalString[:index] + " " + \
        substring + originalString[index + 1:]
    return newString


# to clear the screen and it will invoke the support of ANSI escape sequence of color below.
system("cls")

# print("\033[2J\033[H\033[1;34m============BULK MESSAGE Bomber============")
logo()  # for display the logo
print("\033[1;36m\t\t\t\t\t\t\t\tScripted By: Suraj Kumar Giri\033[0m\n")

originalString = input("\033[1;33m01. Write your message: ")
if originalString == "":  # if user press enter without writing anything
    originalString = "My name is your name"
    print(
        "By default: \033[1;34m'%s'\033[0m will printed as messages.." % originalString
    )

while True:
    try:
        number = int(
            input("\033[1;35m02. How many messages do you want to send: "))
        break
    except ValueError:
        print("\033[1;31mInvalid Input...")
        print("\033[1;32mWrite again..\033[0m")

try:
    interval = float(
        input("\033[1;36m03. Write time interval (in seconds) to send messages: ")
    )
except ValueError:
    print("Input must be in integer or floating point.")
    interval = 0
    print("\033[34mBy default time interval selected to 0")
else:  # in case of no exception
    print("\033[1;32mTime interval = %d selected.." % interval)


choice = input(
    "\033[32m04. Do you want to append index in your string (yes or no) : ")
print(
    "\033[1;31mMessage will be printed at your current cursor position. So, Place your cursor wherever you want to write messages..."
)
print("\033[1;32mYou have 10 seconds to change the cursor position......\033[0m")

string = originalString  # initially string to be printed will originalString

sleep(10)

i = 1
while i <= number:
    if choice == "yes" or choice == "Yes":
        string = addSubStringAfterIndex(
            originalString, len(originalString), str(i))
    write(string)
    press("enter")
    i += 1
    sleep(interval)
