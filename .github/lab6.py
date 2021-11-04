from graphicsCS151 import *
#program should bounce ball across screen
#function creates and draws ball, x and y coordinate are initialized and
def movement1(message, max, min):
    message = input("Enter starting x coordinate ")
    message = int(message)
    x = message
    y = 20
    window = make_window("Ball", 500, 500)
    ball = make_circle(x, y, 10)
    color = color_circle(ball, "red")
    draw_and_color_circle(window, ball, color)
    while(x >= min and x <= max):
        x+=1
        y-=1
        move(ball, x, y)
    sleep(0.5)
    while (x >= min and x <= max):
        x += 1
        y += 1
        move(ball, x, y)
    sleep(0.5)
    while (x >= min and x <= max):
        x -= 1
        y -= 1
        move(ball, x, y)
    sleep(0.5)
    while (x >= min and x <= max):
        x -= 1
        y += 1
        move(ball, x, y)
    sleep(0.5)

    change_title(window, "different direction")
    return x
def main():
    movement1("Enter value", 50, 450)
main()
