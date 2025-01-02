import turtle
import time
import random
#Screen setup
delay = 0.05


#score
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(1)


#snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"


#snake Body

segment = []


#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)


#pen or score on screen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("SCore: 0  High Score: 0", align = "center", font=("courier", 24, "normal"))


#functions


def go_up():
   if head.direction != "down":
    head.direction = "up"

def go_down():
    if head.direction != "up":
     head.direction = "down"
 
def go_left():
    if head.direction != "right":
     head.direction = "left"

def go_right():
   if head.direction != "left":
    head.direction = "right"


#keyboard Binding


wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

def move():
    if head.direction == "up":
      y = head.ycor()
      head.sety(y + 20)

    if head.direction == "down":
      y = head.ycor()
      head.sety(y - 20)

    if head.direction == "left":
      x = head.xcor()
      head.setx(x - 20)

    if head.direction == "right":
      x = head.xcor()
      head.setx(x + 20)


#main game loop


while True:
    wn.update()

    #border collision

    if head.xcor()> 290 or head.xcor() <- 290 or head.ycor() > 290 or head.ycor()<- 290:
       time.sleep(1)
       head.goto(0, 0)
       head.direction = "stop"

      #hide segments
       for segments in segment:
            segments.goto(1000,1000)

            #clear the segment list
            segments.clear()

            #reset score
            score = 0
            delay = .05

            pen.clear()
            pen.write("Score: {}  High score: {}".format(score, high_score), align = "center", font=("courier", 24, "normal"))



    #check for a collision with the food


    if head.distance(food) < 20:
        

     #move the food to a random spot of the screen


        y = random.randint(-290, 290)
        x = random.randint(-290, 290)
        food.goto(x, y)

        #add segment (body section)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

      #shorten delay

        delay -= 0.001

        #increase the Score
        score += 1

        if score > high_score:
          high_score = score

        pen.clear()
        pen.write("Score: {}  High score: {}".format(score, high_score), align = "center", font=("courier", 24, "normal"))


    #move the end segments first in reverse order
    for index in range(len(segment)-1, 0, -1):
          x = segment[index-1].xcor()
          y = segment[index-1].ycor()
          segment[index].goto(x, y)

      #move segment 0 to where the head is
    if len(segment) > 0:
          x = head.xcor()
          y = head.ycor()
          segment[0].goto(x,y)

    move()
    
    #check for head collision with body segments
    for segments in segment:
        if segments.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
                  
            for segment in segment:
                segment.goto(1000,1000)
                segment = []

            score = 0
            delay = .05

            pen.clear()
            pen.write("Score: {}  High score: {}".format(score, high_score), align = "center", font=("courier", 24, "normal"))


    time.sleep(delay)
        

wn.mainloop()