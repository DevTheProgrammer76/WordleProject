#Project Title: Wordle In Python
#Course: CS118 Fundementals of Programming
#Submission Date: 11/25/2025
#Project Type: Group
#Group Members:
#   DB, AH, TT
#File Purpose: Create a working and playable wordle game in python
#Contrubuted to this file: DB, AH, TT


import random as r

def Word_Choice():
    """Creates a list full of wors and randomly assigns one to a text file to be used in the main function"""
    WORDS = ["angry", "apple", "above", "among", "arrow", "armor", "aglet", "ankle", "angle", "below", "bendy", "brown", "break", "black", "brace", "block", "crack", "crown", "cloud", "clown", "crowd", "drown", "dread", "donor", "docks", "dolls", "dusty", "dandy", "daily", "eager", "eagle", "eased", "fight", "fable", "faded", "faces", "gains", "games", "gamma", "grand", "habit", "hacks", "halls", "human", "hyper", "icons", "idiom", "idiot", "ideal", "items", "image", "jolly", "jelly", "jeans", "jacal", "kayak", "kebab", "keeps", "kudos", "label", "labor", "laces", "ladle", "light", "lucky", "magic", "macho", "madly", "nacho", "nails", "naive", "names", "named", "ocean", "oasis", "onion", "older", "price", "paced", "pearl", "petal", "party", "quake", "quart", "quark", "right", "racer", "radar", "rabid", "start", "spoon", "snoop", "scale", "share", "snare", "tight", "tiger", "tired", "trees", "under"]
    secret = r.choice(WORDS)
    file = open("Wordle.txt", "w")
    file.write(secret +"\n")
    file.close()
    return(secret)

Word_Choice()
