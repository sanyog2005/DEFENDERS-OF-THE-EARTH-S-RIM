
import random

import time

def menu():
    print("""             __________________________________________________________________________
             |                                                                         |
             |                                                                         |
             |::::::::::::::::::::::::DEFENDERS OF THE EARTH'S RIM:::::::::::::::::::::|                                                                  
             |                                                                         |
             |                                                                         |             
             |                                                                         |
             |                                                                         |
             |                                                                         |
             |                  ➳      START              [PRESS--1]                  |
             |                                                                         |
             |                                                                         |
             |                                                                         |
             |                  ➳      controls           [PRESS--2]                  |
             |                                                                         |
             |                                                                         |
             |                                                                         |                   
             |                  ➳      ABOUT THE GAME     [PRESS--3]                  |
             |                                                                         |
             |                                                                         |
             |                                                                         |             
             |                  ➳      EXIT GAME          [PRESS--4]                  |
             |                                                                         |
             |                                                                         |
             |                                                                         |
             |                                                                         |
             |                                                                         |             
             |_________________________________________________________________________|                                                                        
           
    """)
    choice=input('                            Enter Task no. From Above:- ')
    print('                            >------------<>------------<')
    if (choice=='1'):
        game()
    #elif(choice=='2'):
      #  print(high_score)
    elif(choice=='2'):
        print("""             __________________________________________________________________________
             |                                                                         |
             |                                                                         |
             |:::::::::::::::::::::::::::::::::CONTROLS::::::::::::::::::::::::::::::::|                                                                  
             |                                                                         |
             |        ✵  TO ACCELARATE FORWARD        PRESS [W]                       |                                                  
             |                                                                         |
             |        ✵  TO DEACCELARATE FORWARD      PRESS [S]                       |                                      
             |                                                                         |
             |        ✵   TO TURN RIGHT               PRESS [D]                       |                                      
             |                                                                         |
             |        ✵   TO ACCELARATE FORWARD       PRESS [A]                       |                                      
             |                                                                         |
             |        ✵  TO FIRE MISSILE              PRESS [SPACE BAR]               |
             |                                                                         |             
             |                                                                         |
             |                                                                         |
             |::::::::::::::::::::::::::::::::::RULES::::::::::::::::::::::::::::::::::|                                                                         
             |                                                                         |
             |        ☛     SHOOTING ALIENS SHIPS{RED}      SCORE INCREASES BY 50     |
             |                                                                         |
             |        ☛     SHOOTING ALLIES SHIPS{BLUE}     SCORE DECREASES BY 20     |
             |                                                                         |             
             |        ☛     COLLIDING ALIENS SHIPS{BLUE}    SCORE DECREASES BY 10     |
             |                                                                         |             
             |_________________________________________________________________________|""")                                                                      
        choice=input('                           press any key to go back to menu:- ')
        print('                            >------------<>------------<')
        if (choice=='m'):
             menu()
        else:
             menu()
        
    elif(choice=='3'):
        print("""             __________________________________________________________________________
             |                                                                         |
             |                                                                         |
             |:::::::::::::::::::::::::::::::ABOUT THE GAME::::::::::::::::::::::::::::|                                                                  
             |                                                                         |
             |                                                                         |             
             |                                                                         |
             |                                                                         |
             |  THE GAME {DEFENDERS OF THE EARTH'S RIM} IS ABOUT THE INVASION OF ALIENS|
             |  SPACE SHIP {RED} ON YOUR PLANET. YOU ARE THE GENERAL OF EARTH          |
             |  SPACE ARMY[E.S.A]. YOU HAVE TO DEFEND THE EARTH IN  YOUR ARK           |   
             |  {WHITE} WITH THE HELP OF YOUR  ALLIES{BLUE }                           |
             |                                                                         |
             |                                                                         |
             |                                                                         |
             |                                                                         |
             |                                                                         |             
             |_________________________________________________________________________|  """ )                                                                     
           
        choice=input('                          press any key to go back to menu:- ')
        print('                            >------------<>------------<')
        if (choice=='m'):
            menu()
        else:
            menu()
    elif(choice=='4'):
        quit()
    else:
        print("wrong choice .Please select the right choice again")
        menu()

def game():
    
    # Import the Turtle module
    import turtle

    # Shows the window
    turtle.fd(0) 
    # Set the animation speed to maximum
    turtle.speed(0)
    # Change the background color
    turtle.bgcolor("black")
    #change background image
   # turtle.bgpic("Untitled.gif")
    #change the window title
    turtle.title(":::::::::::::::::::::::::::::::::DEFENDERS OF EARTH'S RIM::::::::::::::::::::::::::::::::::::")
    # Hide the default turtle
    turtle.ht()
    # This saves memory
    turtle.setundobuffer(1)
    # This speeds up drawing
    turtle.tracer(4) #when we incr objects we have to incr the tracer(frame) to prevent lag 


#to create moving objects for screen
    class Sprite(turtle.Turtle): # turtle.Turtle is parent class of sprite class
#creating a constructor
        def __init__(self, spriteshape, color, startx, starty):
            turtle.Turtle.__init__(self, shape=spriteshape)
            self.speed(0)
            self.penup() #this stops sprites to draw any thing as they keep drawing their path
            self.color(color)
            self.fd(0)
            #starting coordinates of sprites
            self.goto(startx, starty)
            self.speed = 1

        def move(self):
            self.fd(self.speed)

            # Boundary detection
             # here if any sprites reaches border(-300,300) it gets rotated by 60 degree
            #coordinates of sprite remains same
            if self.xcor() > 290:
                self.setx(290)
                self.rt(60)
            if self.xcor() < -290:
                self.setx(-290)
                self.rt(60)
            if self.ycor() > 290:
                self.sety(290)
                self.rt(60)
            if self.ycor() < -290:
                self.sety(-290)
                self.rt(60)

        def is_collision(self, other):
#if cordinates of self(player) came 20 coordinate near to any enemy then there will be a collision
            if (self.xcor() >= (other.xcor() - 20)) and \
            (self.xcor() <= (other.xcor() + 20)) and \
            (self.ycor() >= (other.ycor() - 20)) and \
            (self.ycor() <= (other.ycor() + 20)):
                return True
            else:
                return False
#if any class belongs to a same family the upper classes (parent classes)
#properties will also work for there daughter  classes           

#creating main player 
    class Player(Sprite): #sprite class is parent class of player class
        def __init__(self, spriteshape, color, startx, starty ):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid=1,stretch_len=3,)
            self.speed = 4

#used to turn the sprites to given angle
        def turn_left(self):
            self.lt(45)
        def turn_right(self):
            self.rt(45)
#used to accelarate or deaccelarate 
        def accelerate(self):
            self.speed += 1
        def decelerate(self):
            self.speed -= 1

#creating enemies
    class Enemy(Sprite):
        def __init__(self, spriteshape, color, startx, starty ):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid=1, stretch_len=3, outline=None) 
            self.speed = 4
            self.setheading(random.randint(0,360))#this helps  to move enemy in any random direction when formed
#enemy and allies both will have border detection as thet are child classs of sprite class so propertie is inherted            
    class Ally(Sprite):
        def __init__(self, spriteshape, color, startx, starty ):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid=2, stretch_len=3, outline=None)   
            self.speed = 5
            self.setheading(random.randint(0,360))

        def move(self):
            self.fd(self.speed)

            # Boundary detection
            # here if any sprites reaches border(-300,300) it gets rotated by 60 degree
            #coordinates of sprite remains same
            if self.xcor() > 290: 
                self.setx(290)
                self.lt(60)
            if self.xcor() < -290:
                self.setx(-290)
                self.lt(60)
            if self.ycor() > 290:
                self.sety(290)
                self.lt(60)
            if self.ycor() < -290:
                self.sety(-290)
                self.lt(60)


    class Missile(Sprite):
        def __init__(self, spriteshape, color, startx, starty ):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
            self.speed = 25
            self.status = "ready"# this helps to make it vissible when required
            self.goto(-1000, 1000)

        def fire(self):
            if self.status == "ready":
                
                self.goto(player.xcor(), player.ycor())# this make sure coordinate of missile is coordinate of player 
                self.setheading(player.heading())#this makes missile goes in direction where main player is heading in
                self.status = "firing" # start firring missile

#function to move the missile
        def move(self):

            if self.status == "ready":
                self.goto(-1000,100)

            if self.status == "firing":
                self.fd(self.speed)# this will move missile forwar when staus changes to firring

            # Border check when missile touches border
            if self.xcor() < -290 or self.xcor() > 290 or \
                self.ycor() < -290 or self.ycor() > 290:
                self.goto(-1000,1000)# when missile touches border it will disapier and staus will again change to ready
                self.status = "ready"
#creates heading where score is to be shown
    class Game():
        def __init__(self):
            self.level = 1
            self.score = 0
            self.state = "playing"
            self.pen = turtle.Turtle() # to draw information on screen to show the plawer score
            

        def draw_border(self):
            #Draw border
            self.pen.speed(0)# animation speed
            self.pen.color("black")
            self.pen.pensize(10)#thickness of border
            self.pen.penup()#prevent drawing traces of movement of object 
            self.pen.goto(-300, 300)#coordinates of border
            self.pen.pendown()# draws traces of movement of object 
#creating border as square
            for side in range(4):
                self.pen.fd(600)#moves object 600 coordinate
                self.pen.rt(90)# rotates the object to rotate 90degree
            self.pen.penup()
            self.pen.ht()
            self.pen.pendown()
# creating heading pen
        def show_status(self):
            self.pen.undo()# this doesnot over write score on each other
            msg = "Score: %s" %(self.score)
            self.pen.color("white")
            self.pen.penup()
            self.pen.goto(-300, 310)
            self.pen.write(msg, font=("Arial", 32, "bold"))


    # Create game object
    game = Game()

    # Draw the border
    game.draw_border()

    # Show the game status
    game.show_status()

    # Create the sprites
    player = Player("turtle", "GREY", 0, 0)
    #enemy = Enemy("circle","red", -100, 0)
    missile = Missile("triangle", "yellow", 0, 0)
#creating multiple enemies and allies
    enemies = []# here we take enemy and ally as elements of list
    for i in range(6):
        enemies.append(Enemy("arrow","red", -100, 0))

    allies = []
    for i in range(6):
        allies.append(Ally("classic", "blue", 100, 0))

    #Keyboard bindings used to specify keys for a commond
    turtle.onkey(player.turn_left, "a")
    turtle.onkey(player.turn_right, "d")
    turtle.onkey(player.accelerate, "w")
    turtle.onkey(player.decelerate, "s")
    turtle.onkey(missile.fire, "space")
    turtle.listen()#this helps to commond function

    # Main game loop
    while True:
        turtle.update()#this prevents the screen to update in between the loop now screen will update when loop restarts
        time.sleep(0.001)# helps to delaay the screen to make object move little bit slower

        player.move()
        missile.move()

        for enemy in enemies: #loop to let the enemies move and let the collision of sprites happen between each other for all enemies 
            enemy.move()

            # Check for a collision with the player
            if player.is_collision(enemy):
                #if there will be collision between enemy and player the enemy will teleported to any random coordinate
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                enemy.goto(x, y)# telepotes to random x,y coordinate
                game.score -= 10
                game.show_status()

            # Check for a collision between the missile and the enemy
            if missile.is_collision(enemy):
                #when missile coolides with enemy missile desappiers and enemy is teleported to random direction
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                enemy.goto(x, y)
                missile.status = "ready"
                # Increase the score
                game.score += 50
                game.show_status()

        for ally in allies:#loop to let the all ally move and let the collision of sprites happen between each other for all ally 
            ally.move()

            # Check for a collision between the missile and the ally
            if missile.is_collision(ally):
               #when missile coolides with allies missile desappiers and allies is teleported to random direction
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                ally.goto(x, y)
                missile.status = "ready"
                # Decrease the score
                game.score -= 20
                game.show_status()
        
menu()
