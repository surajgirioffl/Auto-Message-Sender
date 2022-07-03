"""
    Message bomber script. Use to write large number of messages and send them by auto pressing enter. 
"""
from pyautogui import write, press
from time import sleep


def addSubStringAfterIndex(originalString, index, substring):
    '''This function will add passed substring after given index of the string'''
    newString = originalString[:index]+" "+substring+originalString[index+1:]
    return newString


i = 1

originalString = input("Write any string: ")
number = int(input("How many messages do you want to send: "))
print("Do you want to append index in your string (yes or no) : ")
choice = input()
print("\033[1;31mMessage will be printed at your current cursor position. So, Place your cursor wherever you want to write messages...")
print("\033[1;32mYou have 5 seconds to change the cursor position......")

string = originalString  # initially string to be printed will originalString

while i <= number:
    if i == 1:
        sleep(5)
    if(choice == "yes" or choice == "Yes"):
        string = addSubStringAfterIndex(
            originalString, len(originalString), str(i))
    write(string)
    press("enter")
    i += 1
