"""
    Bulk sender script. Use to write large number of messages and send them by auto pressing enter. 
"""
from pyautogui import write, press
from time import sleep


def addSubStringAfterIndex(originalString, index, substring):
    '''This function will add passed substring after given index of the string'''
    newString = originalString[:index]+" "+substring+originalString[index+1:]
    return newString


print("\033[2J\033[H\033[1;34m============BULK MESSAGE SENDER============")
print("\033[1;36m             Scripted By: Suraj Kumar Giri\033[0m\n")

originalString = input("Write any string: ")
if(originalString == ""):  # if user press enter without writing anything
    originalString = "My name is your name"

number = int(input("How many messages do you want to send: "))
choice = input("Do you want to append index in your string (yes or no) : ")
print("\033[1;31mMessage will be printed at your current cursor position. So, Place your cursor wherever you want to write messages...")
print("\033[1;32mYou have 5 seconds to change the cursor position......\033[0m")

string = originalString  # initially string to be printed will originalString

sleep(5)

i = 1
while i <= number:
    if(choice == "yes" or choice == "Yes"):
        string = addSubStringAfterIndex(
            originalString, len(originalString), str(i))
    write(string)
    press("enter")
    i += 1
