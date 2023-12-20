import turtle
import time
import random
import turtle as tur


HALF_WIDTH, HALF_HEIGHT = 700 // 2, 600 // 2 
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

# global variable  para ma track if the game is still running or not
game_running = False

def main():
    global game_running
    game_running = True  # Set the initial state of the game_running 
    racers = get_number_of_racers()
    if racers == 0:
        turtle.bye()  # pra ma close ang graphic window if mag  cancels ang user
    else:
        init_turtle()

        random.shuffle(COLORS)
        colors = COLORS[:racers]

        winner = race(colors)
        print("The winner is the turtle with color:", winner)
        game_running = False  # Set the game_running flag to False

        time.sleep(2) 

def get_number_of_racers():
    # kuha input sa user if pila ang racers
    racers = turtle.numinput('Number of Racers', 'Enter the number of racers (2 - 10): ', minval=2, maxval=10)
    return int(racers) if racers is not None else 0

def race(colors):
    global game_running
    turtles = create_turtles(colors)

    # Countdown animation
    countdown()

    # Wait for a key press to start the race
    turtle.onkey(lambda: turtle.write("Go!", align='center', font=('Arial', 36, 'normal')), 'Return')
    turtle.listen()  


    game_running = True  # Set the game_running  True

    while game_running:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HALF_HEIGHT - 10:
                winner_color = colors[turtles.index(racer)]
                congratulate_winner(winner_color)
                draw_flower_winner()
                game_running = False  # Set the game_running to False
                return winner_color

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

def create_turtles(colors):
    # Create turtle objects for each racer and set their initial positions
    turtles = []
    spacingx = 700 // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-HALF_WIDTH + (i + 1) * spacingx, -HALF_HEIGHT + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    # Initialize the turtle graphics window
    screen = turtle.Screen()
    screen.setup(700, 600)
    screen.title('Turtle Racing!')


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
