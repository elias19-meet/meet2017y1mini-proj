import turtle
#TO FINISH

# make big circle x
# center shapes
# make x go first
# at end of game read board and record results
# at the end of game clear board and start another


def ticTacToe():
    '''logic to be added so a completed game is marked and recorded'''


def draw_grid():
    '''draws a tic-tac-toe grid over the 9 turtle squares'''
    t=turtle.Turtle()
    t.ht()
    t.up()
    t.goto(-40,-40)
    t.down()
    t.forward(240)
    t.left(90)
    t.forward(240)
    t.left(90)
    t.forward(240)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(240)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(240)
    t.left(90)
    t.goto(-40,-40)
    t.left(180)
    t.forward(160)
    t.up()
    t.goto(40,-40)
    t.down()
    t.forward(240)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(240)
def setup_board():
    '''Creates 3 rows of 3 turtles using range(0, 240, 80); turtle.Turtle(); up(); shape('square'); shapesize(4, 4, 4);
    color('white'); goto(x, y). Each turtle is registered to respond to click events using onclick(mark).
    Calls draw_grid() once the 9 turtles are on the board.'''
    for y in range(0,240,80):
        for x in range (0,240,80):
            t=turtle.Turtle()
            t.up()
            t.shape('square')
            t.shapesize(4,4,4,)
            t.color('white')
            t.goto(x,y)
            t.onclick(mark)
    draw_grid()
def mark(x, y):
    '''Function is invoked whenever a turtle registered to respond to click event is clicked. Creates a turtle and draws
    either a circle or an x centered on the x, y coordinates of the click.
    Be sure to set circle to False once the circle is drawn and to True once the x is drawn. '''
    ct = turtle.Turtle()
    ct.ht()
    ct.up()
    global circle
    if circle:
        turtle.goto(x,y)
        turtle.down()
        turtle.circle(20)
        circle = False
    if circle:
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        circle = True

def main():
    wn = turtle.Screen()
    wn.title('tic-tac-toe')
    wn.bgcolor('cyan')
    global circle
    circle = True
    setup_board()
    return 'Done'

if __name__ == '__main__':
    main()
    turtle.TK.mainloop()
