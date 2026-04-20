#Project Title: Wordle In Python
#Course: CS118 Fundementals of Programming
#Submission Date: 11/25/2025
#Project Type: Group
#Group Members:
#   - DB, AH, TT
#File Purpose: Create a working and playable wordle game in python
#Contrubuted to this file: DB, AH, TT


def wordle_grid():
    """Draws the empty wordle grid"""
    import turtle

    x = -265
    y = 225

    t = turtle.Turtle()
    
    t.penup()
    t.goto(-170, 285)
    t.write("WORDLE!", font=("Arial", 50, "bold"))
    t.penup()
    
    while y >= -300:
        t.speed(0)
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.pensize(5)
        t.pendown()
        for i in range(4):
            t.forward(85)
            t.right(90)
    
        t.penup()
        t.goto(-165, y)
        t.pendown()
        for i in range(4):
            t.forward(85)
            t.right(90)

        t.penup()
        t.goto(-65, y)
        t.pendown()
        for i in range(4):
            t.forward(85)
            t.right(90)

        t.penup()
        t.goto(35, y)
        t.pendown()
        for i in range(4):
            t.forward(85)
            t.right(90)
    
        t.penup()
        t.goto(135, y)
        t.pendown()
        for i in range(4):
            t.forward(85)
            t.right(90)
        
        y -= 100
    



import turtle as t

def fill_box(x, y, letter, color, box_size=85):
    """This function allows a letter to be printed in the center of each boc"""
    t.hideturtle()
    t.speed(0)

    # Draw filled square
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(box_size)
        t.right(90)
    t.end_fill()

    # Write the letter in the center
    t.penup()
    t.goto(x + box_size/2, y - box_size + 10)
    t.write(letter.upper(), align="center", font=("Arial", 40, "bold"))
