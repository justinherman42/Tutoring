import random
import turtle




## create global variables
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000  
timer_up = False
my_count=0


## create objects

## object 1 is our turtle which will move places
t=turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(150,50)

## object 2 is our counter, it will update screen with countdown and score
counter =  turtle.Turtle()
counter.hideturtle()


## function to move object turtle t
def move(x,y):
    rx = random.randint(-500,500)
    ry = random.randint(-500,500)
    t.penup()
    t.goto(rx,ry)
    global my_count
    my_count+=1
    global timer
    timer=5
    t.score=my_count
    return(timer,my_count)

#-----countdown writer-----

## function to build countdown clock 
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    endscore= my_count
    ## add endscore attribute to t
    t.endscore = my_count
    ## print final score
    counter.write("Time's Up. Your Final Score is {}".format(endscore), font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer)+" Current score: "+ str(my_count), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


while timer_up == False: 
    wn = turtle.Screen()
    wn.ontimer(countdown, counter_interval) 
    t.onclick(move) 
    turtle.mainloop()


print('FINISHED! FINAL SCORE: {}'.format(t.endscore))