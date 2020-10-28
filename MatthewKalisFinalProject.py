KeySS = False           #Set sentinels for the 2 keys
Keycard = False
FinalDoor = False       #set sentinel for the doo for the main loop
infile = open("savefile", "a")  #open/create save file
print("At any point when you are selecting rooms you may enter 'save' to save the game or you can enter 'load' to load the last save. Also if you would like to clear the last save enter 'clear'.")
print("If you would like to quit, enter 'quit'.")       #main controls
print()         #Empty sapce for formatting
print("You are in an abandoned space station and you must escape to the outside through the airlock door in room 7, but you must collect a keycard to open the door and a space suit so you can survive out in space.") #Intro text
print()
while FinalDoor == False:   #main loop
    print("")
    print("In the centeral room you can go to any of the 7 rooms: Room 1 is the sleeping quarters, Room 2 is secure storage, Room 3 is the greenhouse, Room 4 is the power room, Room 5 is the workshop, Room 6 is the communications room, and room 7 is the airlock.")
    print("Enter either the room you want to explor or any of the commands.")
    RoomSelect = input("")  #Room selection variable
    if RoomSelect == "1":   #Ifs for the different rooms and commands
        print("You walk into the sleeping quarters and you see that all lof the beds are perfetly made, not even a single wrinkle in the pillow, but there doesn't seem to be anything useful in here.")

    elif RoomSelect == "2":
        print("In secure storage you see what look like weapon racks but none of them have any weapons. there also seem to be ammunition creates but the seem empty as well. But on a locked box you see a keypad with just numbers on it, you walk up to enter a code.") #has a consol user must enter a number "22" to get the Keycard
        Kcinput = input("Please enter the code: ")  #Keycard is in this room
        if Kcinput == "22": #User must enter '22' which the find in room 6
            print()
            print("That's correct! The box unlocks with a thud, and inside is a keycard!")
            Keycard = True
        else:
            print("That code didn't work.")

    elif RoomSelect == "3":     #room with the password hint in it
        print("In the greenhouse you feel the tempature change to a humid and damp heat, there is only 1 light working inside of the giant glass dome of a ceiling. Through all of the vines and plants growing in here you feel like you are being watched. But when you look up you see the words 'Mars' written in some red paint on the glass of the dome. You decide you have overstayed your welcome in the greenhouse and walk back to the central hub.") #Has message on wall thats says "Mars" which user must use in room 5 to get Space suit

    elif RoomSelect == "4":
        print("You walk over to the power room. Inside you hear the thrum of the generator and you look around for anything useful. Other then some spare lightbulbs you don't find anything.")

    elif RoomSelect == "5": #User must enter 'Mars' to get the spacesuit they find the password in room 3
        print("You walk to the workshop, and inside you see long worktables and lots of tools. But on the far end of the room you see a space suit locked in a glass case, on the case is a keyboard. You walk over to the keyboard to enter the password.") #User must enter a word "Mars" to get the good space suit
        SSinput = input("Please enter the password: ")
        if SSinput == "Mars":
            print()
            print("That's correct! The case opens up and you get the space suit and put it on!")
            KeySS = True
        else:
            print("That code didn't work")

    elif RoomSelect == "6": #Room with the code hint in it
        print("You go to the communication room, inside you see destroyed radios and broken computers. On the only unbroken screen you see the number '22'.") #puzzle room here with a number on the wall user must enter for the keycard in room 2

    elif RoomSelect == "7":
        print("You go to the airlock.") #Final room which leads out of space station, user must have the Keycard to open the door and a space suit to go outside
        if KeySS == True and Keycard == True:
            FinalDoor = True
            print("You have the keycard and the spacesuit. You unlock the door and walk out on to the surface of the planet. Congratulations! You have won!")
        else:
            print("You did not have bothe the keycard and the spacesuit.")

    elif RoomSelect == "save":  #Save command writes to file if they one or both keys
        infile = open("savefile", "r")
        
        if Keycard == True:
            infile = open("savefile" , "a")
            infile.write("Keycard")
            infile.write("\n")
            infile = open("savefile" , "r")
        
        if KeySS == True:
            infile = open("savefile" , "a")
            infile.write("KSS")
            infile.write("\n")
            infile = open("savefile" , "r")
        infile = open("savefile", "a")
        print("Your progress has been saved!")
        
    elif RoomSelect == "load":  #load command looks if they have any keys in the file. If so set those keys to true.
        infile = open("savefile", "r")
        for line in infile:
            if "Keycard" in line:
                Keycard = True
                print("You have loaded the last save and have the Keycard!")        

        infile = open("savefile", "r")
        for line in infile:
            if "KSS" in line:
                KeySS = True
                print("You have loaded the last save and have the space suit!")       

        infile = open("savefile", "a")
            

    elif RoomSelect == "clear":     #Command to clear the save file
        infile = open("savefile", "w")
        infile = open("savefile", "a")
        print("Your save file has been cleared.")
        

    elif RoomSelect == "quit":  #Quit command to leave the game
        print()
        print("Thank you for playing, see you next time.")
        break
    else:
        print("Please enter a number that corresponds to a room.")
        print("")


infile.close()  #Close the file
