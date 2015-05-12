#For a little extra thing go to line 94 and 103 in my code
# and delete the "#" 

#Implementation of classic arcade game Pong

import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
ScoreA = 0
ScoreB = 0
Color = "Blue"

#extra function -- Ignore it if you like
def change_color():
    global Color
    lis = ["white", "red", "green", "blue", "cyan", "yellow", "magenta"]
    n = random.randrange(0,7)
    Color = lis[n]
    return
    
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global Color
    Color = 'Blue'
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel=[1,1]
    ball_vel[1]= -1* random.randrange(60, 180)
    ball_vel[0]= random.randrange(120,140)
    if direction == "LEFT" :
        ball_vel[0] = - ball_vel[0]

# define event handlers
def new_game():
    global ScoreA, ScoreB  
    ScoreA = 0
    ScoreB = 0
    n = random.randrange(0,3)
    if n == 2:
        dir = 'Right'
    else:
        dir = 'Left'
    spawn_ball(dir)
    
def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, ScoreA, ScoreB, Color
            
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if   ball_pos[1] <= BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
    
    ball_pos[0] += ball_vel[0] / 60
    ball_pos[1] += ball_vel[1] / 60
    

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS ,2, Color, Color)

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos - HALF_PAD_HEIGHT + paddle1_vel / 60 > 0 and paddle1_pos + HALF_PAD_HEIGHT + paddle1_vel / 60 < HEIGHT:
        paddle1_pos += paddle1_vel / 60
    if paddle2_pos - HALF_PAD_HEIGHT + paddle2_vel / 60 > 0 and paddle2_pos + HALF_PAD_HEIGHT + paddle2_vel / 60 < HEIGHT:    
        paddle2_pos += paddle2_vel / 60
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT],[PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos + HALF_PAD_HEIGHT],[0,paddle1_pos + HALF_PAD_HEIGHT]],1, 'WHITE', 'White')
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH,paddle2_pos + HALF_PAD_HEIGHT],[WIDTH - PAD_WIDTH,paddle2_pos + HALF_PAD_HEIGHT]],1, 'WHITE', 'White')
    
    #check if touching sides
    if   ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH :
        if ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT :
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            change_color()
        else:
            ScoreA += 1
            spawn_ball('LEFT')
    elif ball_pos[0] - BALL_RADIUS <= PAD_WIDTH :
        if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT :
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] *= 1.1
            change_color()
        else:
            ScoreB += 1
            spawn_ball('RIGHT')
    
    # draw scores
    canvas.draw_text(str(ScoreA), (150, 80), 40, 'Red')
    canvas.draw_text(str(ScoreB), (450, 80), 40, 'Red') 
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -180.0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 180.0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -180.0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 180.0
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart= frame.add_button('     Restart      ', new_game)


# start frame
new_game()
frame.start()

