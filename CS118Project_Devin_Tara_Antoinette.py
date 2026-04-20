#Project Title: Wordle In Python
#Course: CS118 Fundementals of Programming
#Instructor: Dr. O
#Submission Date: 11/25/2025
#Project Type: Group
#Group Members:
#   - Devin Barrow
#   - Tara Tammo
#   - Antoinette Hults
#File Purpose: Create a working and playable wordle game in python
#Contrubuted to this file: Devin, Tara, Antoinette

#Starts by importing necessary materials for game code
#Imports turtle as t for easy use
import turtle as t
#Imports random as r for easy use
import random as r

#Imports both of the files used to make the code execute properly
import WORDLIST as W
import CS118_Project_Functions as CS

#Directly imports the fill_box function to call it easier
from CS118_Project_Functions import fill_box

#Gives beginning coordinates for the fill_box functions
start_fillX = -265
start_fillY = 325

#Gives the correct function a value for the while lop to start.
correct = "y"
while correct != "n":
    
    #Opens the Wordle.txt file to read the secret answer
    W.Word_Choice()
    file = open("Wordle.txt", "r")
    #A variable that strips the extra lines and reads lines from the text file
    lines = [line.strip().lower() for line in file.readlines()]
    #answer and guess establish the first line is the answer and the rest are guesses
    answer = lines[0]
    guess = lines[1:]
    file.close()

    #Clears the turtle screen then reprints it for clean replayability
    t.clearscreen()
    CS.wordle_grid()
    #Creates a for loop that runs 6 times to assign the user input into the wordle.txt file and compare the guess from the file
    for attempts in range(6):
        file = open("Wordle.txt", "a")
        screen = t.Screen()
        #Creates a input box with turtle for the users guess
        user_word = screen.textinput("Wordle", f"Attempt {attempts + 1}: Enter a 5 letter word!")
        #Input validation: Checks if the user guess is 5 letters
        while len(user_word) != 5:
            user_word = screen.textinput("Wordle", f"Attempt {attempts + 1}: Invalid length Enter a 5 letter word!")
        file.write(user_word.lower() + "\n")
        file.close()
        
        #Subtracts 100 from the Y fill value to fill the next row after a guess
        start_fillY -= 100
            
        #Passes 2 statements, one for the answer and another for guesses
        #This allows the for loop to evaluate the user guess and compare it to the answer
        for i, letter in enumerate(user_word.lower()):
            if letter == answer[i]:
                color = "green"             
            elif letter in answer:
                color = "yellow"
            else:
                color = "gray"
     
            #starts the fill_box function with the color assigned in the for loop above
            fill_box(start_fillX, start_fillY, letter, color)
            start_fillX += 100
        start_fillX -= 500
    
        #Checks if the word is correct
        if user_word == answer:
            correct = screen.textinput("Message", "🎉 You guessed it! Would you like to play again? (y/n)").lower()
            start_fillY = 325
            break
        
    #Runs if the player doesnt guess the word in 6 guesses
    else:
        correct = screen.textinput("Message", f"Sorry, you didn't guess it. The word was {answer}. Would you like to play again(y/n)").lower()
        start_fillY = 325
        
    #Checks the user input to play again    
    if correct != "y":
        t.bye()
        break