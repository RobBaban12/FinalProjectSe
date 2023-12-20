import turtle
import time
import random
import turtle as tur



HALF_WIDTH, HALF_HEIGHT = 700 // 2, 600 // 2 
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def main():
    """
    to  controls the flow of the turtle racing game.
    and initializes the turtles, shuffles the colors, starts the race,
    and prints the winner's color.
    """
    racers = get_number_of_racers()
    if racers == 0:
        turtle.bye()  # Close the graphic window if the user cancels or enters 0
    else:
        init_turtle()

        random.shuffle(COLORS)
        colors = COLORS[:racers]

        winner = race(colors)
        print("The winner is the turtle with color:", winner)

        time.sleep(2)


 
def get_number_of_racers():
    # kuha input sa user if pila ang racers
    racers = turtle.numinput('Number of Racers', 'Enter the number of racers (2 - 10): ', minval=2, maxval=10)
    return int(racers) if racers is not None else 0
#check if the number of racers is within the range of 2 to 10. else return 0

def init_turtle():
    # Initialize the turtle graphics window
    screen = turtle.Screen()
    screen.setup(700, 600)
    screen.title('Turtle Racing!')

def countdown():
    # Display the countdown animation
    counter = turtle.Turtle()
    counter.hideturtle()
    counter.penup()
    counter.setpos(0, 0)

    countdown_text = ["Get Ready", "Set", "Go!"]

    for text in countdown_text:
        counter.write(text, align='center', font=('Arial', 36, 'normal'))
        time.sleep(1)
        counter.clear()
def turtless(colors):

    turtles = []#to store the turtle objects created in the create_turtles function
    spacingx = 700 // (len(colors) + 1)#spacing for between each turtle
    for index, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)# method from turle.Turtle() to set the color of the turtle
        racer.shape('turtle')# by default the shape is arrow shape and turtle shape
        racer.left(90)#to set the direction of the turtle
        racer.penup()#  to lift the pen up
                    #to shift the position of the turtle to the left side 
        racer.setpos(-HALF_WIDTH + (index + 1) * spacingx, -HALF_HEIGHT + 20)# responsible for positioning the turtle on the screen.
        racer.pendown()# to put the pen down
        turtles.append(racer)# append the racer to the list of turtles
    countdown()# here i call the countdown 

    return turtles

def congratulate_winner(winner_color):
    # Display a congratulatory message to the winner
    turtle.Screen()
    congrats_turtle = turtle.Turtle()
    congrats_turtle.hideturtle()
    congrats_turtle.penup()
    congrats_turtle.setpos(0, -50)
    congrats_turtle.write(f"Congratulations, {winner_color} turtle! here is your flower!",
                          align='center', font=('Arial', 20, 'normal'))
    time.sleep(2)
    
def race(colors):
    turtles = turtless(colors)

    game_running = True  # Set the game_running  True
    while game_running:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            _, y = racer.pos()
            if y >= HALF_HEIGHT - 10:
                winner_color = colors[turtles.index(racer)]
                congratulate_winner(winner_color)
                draw_flower_winner()
                return winner_color
       




def draw_flower_winner():
    # Draw a flower as a reward for the winner
    screen = turtle.Screen()
    for item in screen.turtles():
        item.hideturtle()
        item.clear()

    tur.title("Draw a Rose")

    # Set initial position
    tur.penup()
    tur.left(90)
    tur.fd(200)
    tur.pendown()
    tur.right(90)

    # flower base
    tur.fillcolor("red")
    tur.begin_fill()
    tur.circle(10, 180)
    tur.circle(25, 110)
    tur.left(50)
    tur.circle(60, 45)
    tur.circle(20, 170)
    tur.right(24)
    tur.fd(30)
    tur.left(10)
    tur.circle(30, 110)
    tur.fd(20)
    tur.left(40)
    tur.circle(90, 70)
    tur.circle(30, 150)
    tur.right(30)
    tur.fd(15)
    tur.circle(80, 90)
    tur.left(15)
    tur.fd(45)
    tur.right(165)
    tur.fd(20)
    tur.left(155)
    tur.circle(150, 80)
    tur.left(50)
    tur.circle(150, 90)
    tur.end_fill()

    # Petal 1
    tur.left(150)
    tur.circle(-90, 70)
    tur.left(20)
    tur.circle(75, 105)
    tur.setheading(60)
    tur.circle(80, 98)
    tur.circle(-90, 40)

    # Petal 2
    tur.left(180)
    tur.circle(90, 40)
    tur.circle(-80, 98)
    tur.setheading(-83)

    # Leaves 1
    tur.fd(30)
    tur.left(90)
    tur.fd(25)
    tur.left(45)
    tur.fillcolor("green")
    tur.begin_fill()
    tur.circle(-80, 90)
    tur.right(90)
    tur.circle(-80, 90)
    tur.end_fill()
    tur.right(135)
    tur.fd(60)
    tur.left(180)
    tur.fd(85)
    tur.left(90)
    tur.fd(80)

    # Leaves 2
    tur.right(90)
    tur.right(45)
    tur.fillcolor("green")
    tur.begin_fill()
    tur.circle(80, 90)
    tur.left(90)
    tur.circle(80, 90)
    tur.end_fill()
    tur.left(135)
    tur.fd(60)
    tur.left(180)
    tur.fd(60)
    tur.right(90)
    tur.circle(200, 60)

    tur.done()

if __name__ == "__main__":
    main()
