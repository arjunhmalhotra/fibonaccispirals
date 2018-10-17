#################################### FIBONACCI SPIRAL #######################################

import math

import turtle

def fibRecSpiral(asteroid, progress):

    '''

    This function defines the Rectangular and spiral drawing functions and the path for the turtle to take.

    The function name is fibRecSpiral
    The output is a rectangle and a spiral running from one corner to the other inside the rectangle.
    The inputs are the path descriptions for the turtle to take. in this case, asteroid and progress.

    '''

    asteroid.pensize(1)                         #for both the rectangle and the resulting spiral
    asteroid.pencolor('black')
    for i in range(4):
        asteroid.forward(progress)
        asteroid.left(90)

    asteroid.pensize(2)
    asteroid.pencolor('purple')
    asteroid.circle(progress, 90, 45)

    
############################################

def sequence(num):

    '''

    This function defines the overarching mathematical repetition of the previous function.

    This function is called 'sequence'.
    This function's inputs are the fibonacci sequence.
    The function gives a mathematical output as a value for the repetition of the for loop
    in the turtle function.

    '''
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return sequence(num-1) + sequence(num-2)



############################################

#defining the turtle graphics module

def main():

    '''

    This is the turtle module for the code.

    The inputs are the turtle object, the speed of the turtle, the appearance, it's speed,
    and the path's it should repeat.
    The output is the graphical result desired.

    '''

    pokemon = turtle.Turtle()
    pokemon.hideturtle()
    pokemon.setheading(0)
    pokemon.speed(20)

    for i in range(20):
        
        progress = sequence(i+1)*5
        fibRecSpiral(pokemon, progress)

    screen = pokemon.getscreen()
    screen.exitonclick()

main()

############################################### END ######################################
    
