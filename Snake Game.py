# snake game 
# importing modules
import turtle
import random
# programm constrains
WIDTH = 500
HEIGHT = 500
DELAY = 100
FOOD_SIZE = 10
offsets = {
    "up": (0,20),
    "down": (0,-20),
    "left": (-20,0),
    "right": (20,0)
}

# direction
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"
def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"
def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"
def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"
# game_loop
def game_loop():
    stamper.clearstamps()
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]
    # change if collision occurs
    if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2 :
        reset()
    else:

         # add new head
        snake.append(new_head)
        if not food_collision():
            snake.pop(0)

        #draw
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
        #refresh screen
        screen.title(f"Snake Game. Score:{score}")
        screen.update()

       #rinse and repeat
        turtle.ontimer(game_loop, DELAY)

def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0,0], [20,0], [40,0], [60,0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()

# food collision
def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

#get random_food
def get_random_food_pos():
    x = random.randint(-WIDTH/2 + FOOD_SIZE, WIDTH/2 - FOOD_SIZE)
    y = random.randint(-HEIGHT/2 + FOOD_SIZE, HEIGHT/2 - FOOD_SIZE)
    return (x,y)
#get distanc
def get_distance(pos1, pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    distance = ((y2 - y1) **2 + (x2 - x1) **2)**0.5
    return distance

# Creat a window for game
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("Snake Game")
screen.bgcolor("yellow")
screen.tracer(0)
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# create turtle to do your biding
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.penup()

# food
food = turtle.Turtle()
food.shape("triangle")
food.color("red")
food.shapesize(FOOD_SIZE/20)
food.penup()

reset()
turtle.done()