import turtle
02
#TO FINISH
03
 
04
# make big circle x
05
# center shapes
06
# make x go first
07
# at end of game read board and record results
08
# at the end of game clear board and start another
09
 
10
 
11
def ticTacToe():
12
    '''logic to be added so a completed game is marked and recorded'''
13
 
14
 
15
def draw_grid():
16
    '''draws a tic-tac-toe grid over the 9 turtle squares'''
17
    t=turtle.Turtle()
18
    t.ht()
19
    t.up()
20
    t.goto(-40,-40)
21
    t.down()
22
    t.forward(240)
23
    t.left(90)
24
    t.forward(240)
25
    t.left(90)
26
    t.forward(240)
27
    t.left(90)
28
    t.forward(80)
29
    t.left(90)
30
    t.forward(240)
31
    t.right(90)
32
    t.forward(80)
33
    t.right(90)
34
    t.forward(240)
35
    t.left(90)
36
    t.goto(-40,-40)
37
    t.left(180)
38
    t.forward(160)
39
    t.up()
40
    t.goto(40,-40)
41
    t.down()
42
    t.forward(240)
43
    t.right(90)
44
    t.forward(80)
45
    t.right(90)
46
    t.forward(240)
47
def setup_board():
48
    '''Creates 3 rows of 3 turtles using range(0, 240, 80); turtle.Turtle(); up(); shape('square'); shapesize(4, 4, 4);
49
    color('white'); goto(x, y). Each turtle is registered to respond to click events using onclick(mark).
50
    Calls draw_grid() once the 9 turtles are on the board.'''
51
    for y in range(0,240,80):
52
        for x in range (0,240,80):
53
            t=turtle.Turtle()
54
            t.up()
55
            t.shape('square')
56
            t.shapesize(4,4,4,)
57
            t.color('white')
58
            t.goto(x,y)
59
            t.onclick(mark)
60
    draw_grid()
61
def mark(x, y):
62
    '''Function is invoked whenever a turtle registered to respond to click event is clicked. Creates a turtle and draws
63
    either a circle or an x centered on the x, y coordinates of the click.
64
    Be sure to set circle to False once the circle is drawn and to True once the x is drawn. '''
65
    ct = turtle.Turtle()
66
    ct.ht()
67
    ct.up()
68
    global circle
69
    if circle:
70
        turtle.goto(x,y)
71
        turtle.down()
72
        turtle.circle(20)
73
        circle = False
74
    if circle:
75
        turtle.up()
76
        turtle.goto(x,y)
77
        turtle.down()
78
        circle = True
79
 
80
def main():
81
    wn = turtle.Screen()
82
    wn.title('tic-tac-toe')
83
    wn.bgcolor('cyan')
84
    global circle
85
    circle = True
86
    setup_board()
87
    return 'Done'
88
 

if __name__ == '__main__':

    main()

    turtle.TK.mainloop()
