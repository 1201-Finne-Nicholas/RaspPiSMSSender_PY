#Importing OS to use command lines

import os

#Starter menu for the user
while True:

    menuInput = input("1. Add new phone number \n\n2. See current phone numbers \n\n3. Send a message to the list of numbers \n\n4. Clear all numbers on list \n\n5. Exit \n\n")

    #   Menu's Sections
    if (menuInput == "1"): 
        # Adds new numbers
        PhoneNumbers = open("PhoneNumbersList.txt", "a+")
        newPN = input("Type in phone number:\n")
        PhoneNumbers.write(newPN)
        PhoneNumbers.write("\n")
        PhoneNumbers.close()
        
    elif (menuInput == "2"): 
        # Reads out numbers
        PhoneNumbers = open("PhoneNumbersList.txt", "r")
        numbers = PhoneNumbers.read()
        print(numbers)
        PhoneNumbers.close()
    elif (menuInput == "3"):
        textMessage = input("\nWhat would you like to send out to the phone numbers?\n")
        PhoneNumbers = open("PhoneNumbersList.txt", "r")
        pnumbers = PhoneNumbers.readlines()
        i = 0
        for x in pnumbers:
            if(pnumbers != ""):
                print('echo "{0}" | sudo gammu sendsms TEXT {1}' .format(textMessage, pnumbers[i]))
                #os.system('echo "{0}" | sudo gammu sendsms TEXT {1}' .format(textMessage, pnumbers))
                i = i + 1
    elif (menuInput == "4"): 
        # Clears all numbers
        PhoneNumbers = open("PhoneNumbersList.txt", "w+")
        PhoneNumbers.write("")
    elif (menuInput == "5"): 
        # Exits app
        print("Exiting")
        break
