from turtle import Turtle, Screen

slo = Turtle()
screen = Screen()


def move_forwards():
    slo.forward(10)


def move_backwards():
    slo.backward(10)


def turn_left():
    slo.left(10)


def turn_right():
    slo.right(10)


def clear_screen():
    slo.clear()
    slo.penup()
    slo.home()
    slo.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
