#This is a MadLibs project 
#My name: Melanie Vang
#Who I collaborated with: Joel Villa, Fedora Yang, Julissa Talaroc, Dominique Harden

print("************************************")
print("|                                  |")
print("|      Welcome to MadLibs          | ") 
print("|                                  |")
print("************************************") #Add quotions

("""MadLibs is a fill-in-the-blanks story
game. The player must choose words based on the 
given prompts, and the computer will return a 
short story that includes the words the user chose.""") #added and fixed triple quotations

play = input("Do you want to play MadLibs?(y/n) ") #changed input to output

if play == "y": #added another equal sign and colon to show what to do when condition is met
    person_name = input("Choose a name for a person: ")
    place = input("Choose a place: ")
    noun_1 = input("Choose a singlular noun: ")
    animal_1 = input("Choose an animal: ") #added quotations marks 
    adjective_1 = input("Choose an adjective for a feeling: ")
    adjective_2 = input("Choose an adjective: ")
    adjective_3 = input("Choose an adjective: ") #added equal sign
    animal_2 = input("Choose an animal: ")
    food = input("Choose a food: ")
    
    print("""
    Over break I am going camping with """ +person_name+""". It is important 
    to be prepared when camping at """ +place+""" , so I made sure to pack a 
    sleeping bag, flashlight, and a """ +noun_1+""". The possibility of seeing a 
    """ +animal_1+""" makes me feel """ +adjective_1+""". I am excited to go 
    hiking on the """ +adjective_2+""" trail. If I see a """ +adjective_3 +""" """ +animal_2+""" 
    on the hike, I will take it home as my new pet! The best part of 
    camping is eating """ +food+""" by the campfire!
    """) #changed place to the string
    
    print("Thanks for playing! Goodbye!")
else:
    print("Goodbye!") #indenteted
    
    
