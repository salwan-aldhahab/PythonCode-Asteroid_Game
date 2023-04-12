import turtle
import time
import random
import math
import winsound

# Beginning / Start Sound Track
winsound.PlaySound("2001 A Space Odyssey Theme song", winsound.SND_ASYNC)

# Player Object
player = turtle.Turtle()

# Screen Object
screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgpic("space_bg.png")
screen.tracer(2)

# Adding Shapes / Images
screen.addshape("polygon_player.gif")
screen.addshape("asteroid.gif")
screen.addshape("black-hole.gif")

# Player Object Specifications
player.left(90)
player.shape("polygon_player.gif")
player.color("white")
player.penup()
player.speed(0)

# Boundary / Wall Object
wall = turtle.Turtle()
wall.shape("blank")
wall.penup()
wall.setposition(-250, -250)
wall.pendown()
wall.pencolor("yellow")
wall.pensize(5)
wall.speed(0)

for side in range(4):
    wall.forward(500)
    wall.left(90)

# Welcome Message & Creator Name
wall.penup()
wall.setposition(-250, -280)
wall.write("Created By Salwan Aldhahab", font=("Arial", 10, "bold"))
wall.pencolor("red")
wall.setposition(-230, 42)
wall.write("Welcome to The Asteroid Game", font=("Arial", 18, "bold"))

# Timer Object
timer_screen = turtle.Turtle()
timer_screen.shape("blank")
timer_screen.penup()
timer_screen.pencolor("white")
timer_screen.setposition(-100, 0)
timer_screen.write("Press The \"Space\" Key\nto Start The Game :)", font=("Arial", 14, "bold"))

# Score Object / Screen / Counter
score_screen = turtle.Turtle()
score_screen.shape("blank")
score_screen.pencolor("yellow")
score_screen.penup()
score_screen.speed(0)
score_screen.setposition(160, 220)
score_screen.write("Score: 0", font=("Arial", 12, "bold"))

# Speed Screen Object
speed_screen = turtle.Turtle()
speed_screen.shape("blank")
speed_screen.pencolor("yellow")
speed_screen.penup()
speed_screen.speed(0)
speed_screen.setposition(-30, 220)
speed_screen.write("Speed: 0", font=("Arial", 12, "bold"))


class Control:

    def __init__(self):
        # Start Speed & Angle
        self.speed_player = 1
        self.angle = 30

        # Start Score
        self.score = 0

        # Boundary Coordinate
        # Absolute Value For Y & X Coordinates
        self.boundary_coord = 232

        # Time Limit & Object
        self.time_limit = 45              # 45 Seconds is The Time Limit
        self.start_time = time.time()     # Returning Current Time

        # Random Object
        self.random = random.Random()

        # Turtle Game Asteroids Initiate List Objects
        self.asteroids = []
        self.asteroid = None

        # Black Holes Initiate List Objects
        self.black_holes = []
        self.black_hole = None

    def updating_speed(self):
        # Speed Counter -- Updates / Writes Current Speed of The Player
        speed_screen.write(f"Speed: {self.speed_player:+.0f}", font=("Arial", 12, "bold"))

    def get_elapsed_time(self):
        # Getting Elapsed Time & Returning The Remaining Time
        elapsed_time = time.time() - self.start_time
        remaining_time = self.time_limit - elapsed_time
        return int(remaining_time)

    def player_reappearing(self):
        # Walls Condition Statement For The Player Object
        # Ship Goes Through The Wall / Reappearing Other Side of The Wall 
        # x-axis  (Right & Left Sides of The Wall)
        if player.xcor() > self.boundary_coord or player.xcor() < -self.boundary_coord:
            player.setposition(x=-player.xcor(), y=player.ycor())
            winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        # y-axis (Upper & Lower Sides of The Wall)
        if player.ycor() > self.boundary_coord or player.ycor() < -self.boundary_coord:
            player.setposition(x=player.xcor(), y=-player.ycor())
            winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    def creating_asteroids(self):
        # Creating Asteroid Objects
        for obj in range(6):
            self.asteroids.append(turtle.Turtle())

        # Setting Asteroids Specifications
        for self.asteroid in self.asteroids:
            self.asteroid.shape("asteroid.gif")
            self.asteroid.penup()
            self.asteroid.setposition(
                x=self.random.randint(-self.boundary_coord, self.boundary_coord),
                y=self.random.randint(-self.boundary_coord, self.boundary_coord)
            )

    def asteroid_reappearing(self):
        # Boundaries / Asteroid Reappear
        # Asteroid Reappear On a Random Place On The Other Side of The Wall
        # x-axis
        if self.asteroid.xcor() > self.boundary_coord:      # Right Side Wall Condition Statement
            self.asteroid.setposition(
                x=-self.boundary_coord,
                y=self.random.randint(-self.boundary_coord, self.boundary_coord)
            )
        elif self.asteroid.xcor() < -self.boundary_coord:   # Left Side Wall Condition Statement
            self.asteroid.setposition(
                x=self.boundary_coord,
                y=self.random.randint(-self.boundary_coord, self.boundary_coord))

        # y-axis
        if self.asteroid.ycor() > self.boundary_coord:      # Upper Side Wall Condition Statement
            self.asteroid.setposition(
                x=self.random.randint(-self.boundary_coord, self.boundary_coord),
                y=-self.boundary_coord
            )
        elif self.asteroid.ycor() < -self.boundary_coord:   # Lower Side Wall Condition Statement
            self.asteroid.setposition(
                x=self.random.randint(-self.boundary_coord, self.boundary_coord),
                y=self.boundary_coord
            )

    def detecting_player_collision(self):
        # Distance Between Player & Asteroids
        # Distance Formula d=√((x2-x1)^2+(y2-y1)^2)
        d_1 = math.sqrt(
            math.pow(player.xcor()-self.asteroid.xcor(), 2) +
            math.pow(player.ycor()-self.asteroid.ycor(), 2)
        )

        if d_1 < 30:
            # Distance Limit Between Player & Asteroids
            winsound.PlaySound("Collision.wav", winsound.SND_ASYNC)
            self.asteroid.setposition(
                x=-self.boundary_coord,
                y=self.random.randint(-self.boundary_coord, self.boundary_coord)
            )
            score_screen.undo()     # Deleting Last Score Written
            self.score += 1         # Counting 1 Score Up If Collision Detected
            score_screen.write(f"Score: {self.score}", font=("Arial", 12, "bold"))

    def creating_black_holes(self):
        # Creating Black Hole Objects
        for obj in range(4):
            self.black_holes.append(turtle.Turtle())

        # Setting Black Holes Specifications
        for self.black_hole in self.black_holes:
            self.black_hole.shape("black-hole.gif")
            self.black_hole.penup()
            self.black_hole.setposition(x=self.random.randint(-220, 220), y=self.random.randint(-220, 220))

    def hyperspace_jump(self):
        # Distance Between Player & Black Holes
        # Distance Formula d=√((x2-x1)^2+(y2-y1)^2)
        d_2 = math.sqrt(
            math.pow(player.xcor()-self.black_hole.xcor(), 2) +
            math.pow(player.ycor()-self.black_hole.ycor(), 2)
        )

        # Distance Between Black Holes & Asteroids
        # Distance Formula d=√((x2-x1)^2+(y2-y1)^2)
        d_3 = math.sqrt(
            math.pow(self.black_hole.xcor()-self.asteroid.xcor(), 2) +
            math.pow(self.black_hole.ycor()-self.asteroid.ycor(), 2)
        )

        if d_2 < 40:
            # Distance Limit Between Player & Black Holes
            winsound.PlaySound("jump.wav", winsound.SND_ASYNC)
            player.setposition(
                x=self.random.randint(-self.boundary_coord, self.boundary_coord),
                y=self.random.randint(-self.boundary_coord, self.boundary_coord)
            )
        elif d_3 < 40:
            # Distance Limit Between Black Holes & Asteroids
            self.asteroid.setposition(
                x=self.random.randint(-self.boundary_coord, self.boundary_coord),
                y=self.random.randint(-self.boundary_coord, self.boundary_coord)
            )
            # Random Turn If The Asteroid Jump Through a Black Hole
            random_turn = [
                self.asteroid.right(self.random.randint(0, 180)),
                self.asteroid.left(self.random.randint(0, 180))
            ]
            self.random.choice(random_turn)

    def start_game(self):
        # By pressing on the "space" key this method will be activated

        wall.undo()            # Deleting Welcome Message
        timer_screen.undo()    # Deleting "Space" Key Message

        timer_screen.setposition(-230, 220)    # re-positioning timer object
        timer_screen.pencolor("yellow")
        timer_screen.speed(0)

        self.creating_asteroids()  # Activating Asteroids
        self.creating_black_holes()  # Activating Black Holes

        while True:
            # Player Move / Speed
            player.forward(self.speed_player)

            # Player Speed Monitor/Screen
            speed_screen.undo()
            self.updating_speed()

            # Asteroids Move
            for self.asteroid in self.asteroids:
                self.asteroid.forward(1)
                self.asteroid_reappearing()
                self.detecting_player_collision()

            # Checking For a Black Hole For The Player & Asteroids
            # If Black Hole Detected, Then Hyperspace Jump To a Random Place
            for self.black_hole in self.black_holes:
                for self.asteroid in self.asteroids:
                    self.hyperspace_jump()

            # Activating 'Player Reappearing On The Other Side of Wall If It Hits Wall' Method
            self.player_reappearing()

            # Deleting / Re-writing Time
            timer_screen.undo()

            # Loop Break & Timer ---- "Ending The Game"  Condition Statement
            if 0 < self.get_elapsed_time() <= self.time_limit:
                timer_screen.write(f"Timer: {self.get_elapsed_time()}s", font=("Arial", 12, "bold"))
            else:
                timer_screen.setposition(-80, 0)
                timer_screen.pencolor("red")
                timer_screen.write("Game Over", font=("Arial", 24, "bold"))
                timer_screen.pencolor("white")
                timer_screen.setposition(-115, -20)
                timer_screen.write("Press \"Esc\" to Exit Game", font=("Arial", 14, "bold"))
                winsound.PlaySound("Game Over.wav", winsound.SND_ASYNC)
                break

    def increase_speed(self):
        # Player Speed Increase Method
        if 1 <= self.speed_player < 5:    # Speed Limited Between 1 to 5
            winsound.PlaySound("Speed.wav", winsound.SND_ASYNC)
            self.speed_player += 1
        else:
            self.speed_player = self.speed_player   # Don't Change Speed If Speed Limit Reached

    def decrease_speed(self):
        # Player Speed Decrease Method
        if 1 < self.speed_player:         # If Higher Than 1 By Pressing Down Key Speed Will Decrease
            winsound.PlaySound("Speed.wav", winsound.SND_ASYNC)
            self.speed_player -= 1
        else:
            self.speed_player = self.speed_player  # Else Don't Change Speed

    def turn_right(self):
        # Right Turn Method
        player.right(self.angle)

    def turn_left(self):
        # Left Turn Method
        player.left(self.angle)


# Activating / Creating Object Class Control
control_player = Control()

# Keyboard Keys Commands
turtle.listen()
turtle.onkey(control_player.start_game, "space")
turtle.onkeypress(control_player.increase_speed, "Up")
turtle.onkeypress(control_player.decrease_speed, "Down")
turtle.onkeypress(control_player.turn_right, "Right")
turtle.onkeypress(control_player.turn_left, "Left")
turtle.onkey(screen.bye, "Escape")

turtle.done()
