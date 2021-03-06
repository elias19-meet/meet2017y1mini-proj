import turtle
import random
color=0
turtle.tracer(1,0)
counter=1
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()
SQUARE_SIZE=20
START_LENGTH=1
turtle.color("red")
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]
snake=turtle.clone()
snake.shape('circle')
turtle.hideturtle()
snake.color("green")

box=turtle.clone()

box.goto(0,250)
box.pendown()
box.goto(400,250)
box.goto(-400,250)
box.goto(-400,-250)
box.goto(400,-250)
box.goto(400,250)


    
    
for s in range (START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    stamp_id=snake.stamp()
    stamp_list.append(stamp_id)

    
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR="space"
UP=0
DOWN=1
LEFT=2
RIGHT=3
    
direction=UP

UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400


def up():
    global direction
    if direction !=DOWN:
        direction=UP
    print("you moved up !!")
    
def down():
    global direction
    if direction != UP:
        direction=DOWN
    print("you moved down !!")

def left():
    global direction
    if direction !=RIGHT:
        direction=LEFT
    print("you moved left !! ")

def right():
    global direction
    if direction !=LEFT:
        direction=RIGHT
    print("you moved right !!")

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

food=turtle.clone()
food.color("orange")
food.shape("square")
food.hideturtle()

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    
    food_position = (food_x,food_y)
    food.goto(food_position)
    food_pos.append(food_position)
    l = food.stamp()
    food_stamps.append(l)
    
    
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print("you moved right")
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print("you moved left !!")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("you moved up !!")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
    
        
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    
    
    global food_stamps,food_pos
    if snake.pos() in food_pos:
        global counter
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        #stamp_list.append(snake.pos())
        print("you have eaten the food!")
        counter=counter+1
        turtle.clear()
        turtle.write(counter,font=(20))
        print(counter)
        make_food()
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
        



    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    
    if new_x_pos>=RIGHT_EDGE:
        print("GAME OVER !!! YOU HIT THE RIGHT EDGE ")
        quit()
    if new_x_pos<=LEFT_EDGE:
        print("GAME OVER !!! YOU HIT THE LEFT EDGE ")
        quit()
    if new_y_pos<=DOWN_EDGE:
        print("GAME OVER !!! YOU HIT THE LOWER EDGE ")
        quit()
    if new_y_pos>=UP_EDGE:
        print("GAME OVER !!! YOU HIT THE UPPER EDGE ")
        quit()
    if snake.pos() in pos_list[0:-1]:
        quit()
    turtle.ontimer(move_snake,TIME_STEP)
    
move_snake()
make_food()


    
    
###########################################################################











    
