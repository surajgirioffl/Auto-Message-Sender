"""
    Bulk sender script. Use to write large number of messages and send them by auto pressing enter. 
"""
from pyautogui import write, press
from time import sleep
from os import system


def addSubStringAfterIndex(originalString, index, substring):
    '''This function will add passed substring after given index of the string'''
    newString = originalString[:index]+" "+substring+originalString[index+1:]
    return newString


# to clear the screen and it will invoke the support of ANSI escape sequence of color below.
system("cls")

print("\033[2J\033[H\033[1;34m============BULK MESSAGE SENDER============")
print("\033[1;36m             Scripted By: Suraj Kumar Giri\033[0m\n")

originalString = input("Write any string: ")
if(originalString == ""):  # if user press enter without writing anything
    originalString = "My name is your name"
    print("By default: \033[1;34m'%s'\033[0m will printed as messages.." % originalString)

while(True):
    try:
        number = int(input("How many messages do you want to send: "))
        break
    except ValueError:
        print("\033[1;31mInvalid Input...")
        print("\033[1;32mWrite again..\033[0m")

try:
    interval = float(input("Write time interval (in seconds) to send messages: "))
except ValueError:
    print("Input must be in integer or floating point.")
finally:
    interval = 0
    print("\033[34mBy default time interval selected to 0")

choice = input("\033[32mDo you want to append index in your string (yes or no) : ")
print("\033[1;31mMessage will be printed at your current cursor position. So, Place your cursor wherever you want to write messages...")
print("\033[1;32mYou have 10 seconds to change the cursor position......\033[0m")

string = originalString  # initially string to be printed will originalString

sleep(10)

i = 1
while i <= number:
    if(choice == "yes" or choice == "Yes"):
        string = addSubStringAfterIndex(
            originalString, len(originalString), str(i))
    write(string)
    press("enter")
    i += 1
    sleep(interval)
