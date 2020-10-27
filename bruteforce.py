import random
import pyautogui
import string


#If you use a password that has more than 4 characters it takes a while
allChars = "abcdefghijklmnopqrstuvwxyz0123456789"

# allChars = string.printable
allChars_list = list(allChars)


password = pyautogui.password("Enter a password : ")

genPass = ""

while(genPass != password):
    genPass = random.choices(allChars_list, k=len(password))

    print("<=================="+ str(genPass)+ "==================>")

    if(genPass == list(password)):
        print("Your password is : "+ "".join(genPass))
        input()