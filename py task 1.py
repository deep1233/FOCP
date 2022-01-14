print("Stop! Who would cross the Bridge of Death")
print("Must answer me these questions three, 'ere the other side he see.")

#Asks for input a name 
name=input("What is your name?")


#Checks if he is king or not
if name.capitalize()=="Arthur":
    print("My liege! You may pass!")
else:
    #Asks for the quest
    quest = input("what is your quest?")
    
    #checking if the quest contains "grail" or not
    if "grail" in quest.lower():
        
        #Asks for the favourite colour
        colour = input("What is your favourite color?")

        #Checks if the first letter of the name and colour is same or not
        if colour[0].upper() == name[0].upper():
            print("You may pass!!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    
    else:
        print("Only those who seek the (Grail) may pass")
