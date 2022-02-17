"""ex04 Getting familiar with turtle and function uses."""
from turtle import Turtle, colormode, done
colormode(255)

PEN: Turtle = Turtle()

HOUSE_X: float = -50.0
HOUSE_Y: float = -50.0

WINDOW_X: float = -30.0
WINDOW_Y: float = 0.0

ROOF_X = HOUSE_X
ROOF_Y = HOUSE_Y + 100

DOOR_X = HOUSE_Y + 40
DOOR_Y = HOUSE_Y


def base_house(pen: Turtle, x: float, y: float) -> None:
    """Base of the house."""
    BASE_HOUSE_LENGTH: int = 100
    ANGLE_BASE_HOUSE: int = 90
    R_BASE: int = 168
    G_BASE: int = 36
    B_BASE: int = 0
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(R_BASE, G_BASE, B_BASE)
    pen.fillcolor(R_BASE, G_BASE, B_BASE)
    pen.begin_fill()
    i: int = 0
    SIDES: int = 4
    while i < SIDES:
        pen.forward(BASE_HOUSE_LENGTH)
        pen.left(ANGLE_BASE_HOUSE)
        i += 1
    pen.end_fill()


def windows(pen: Turtle, x: float, y: float) -> None:
    """Windows of the house."""
    LENGTH_WINDOW: int = 20
    WIDTH_WINDOW: int = 10
    ANGLE_WINDOW: int = 90
    R_WINDOW: int = 0
    G_WINDOW: int = 0
    B_WINDOW: int = 0
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(R_WINDOW, G_WINDOW, B_WINDOW)
    pen.fillcolor(R_WINDOW, G_WINDOW, B_WINDOW)
    pen.begin_fill()
    i: int = 0
    SIDES: int = 2
    while i < SIDES:
        pen.forward(WIDTH_WINDOW)
        pen.left(ANGLE_WINDOW)
        pen.forward(LENGTH_WINDOW)
        pen.left(ANGLE_WINDOW)
        i += 1
    pen.end_fill()


def roof(pen: Turtle, x: float, y: float) -> None:
    """ROOF OF THE HOUSE."""
    LENGTH_ROOF: int = 100
    ANGLE_ROOF: int = 120
    R_ROOF: int = 135
    G_ROOF: int = 65
    B_ROOF: int = 0
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(R_ROOF, G_ROOF, B_ROOF)
    pen.fillcolor(R_ROOF, G_ROOF, B_ROOF)
    pen.begin_fill()
    i: int = 0
    SIDES: int = 3
    while i < SIDES:
        pen.forward(LENGTH_ROOF)
        pen.left(ANGLE_ROOF)
        i += 1
    pen.end_fill()


def door(pen: Turtle, x: float, y: float) -> None:
    """Door of the house."""
    LENGTH_DOOR: int = 25
    WIDTH_DOOR: int = 20
    ANGLE_DOOR: int = 90
    R_DOOR: int = 135
    G_DOOR: int = 65
    B_DOOR: int = 0
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(R_DOOR, G_DOOR, B_DOOR)
    pen.fillcolor(R_DOOR, G_DOOR, B_DOOR)
    pen.begin_fill()
    i: int = 0
    SIDES: int = 2
    while i < SIDES:
        pen.forward(WIDTH_DOOR)
        pen.left(ANGLE_DOOR)
        pen.forward(LENGTH_DOOR)
        pen.left(ANGLE_DOOR)
        i += 1
    pen.end_fill()


def main() -> None:
    """Calls all functions."""
    base_house(PEN, HOUSE_X, HOUSE_Y)
    windows(PEN, WINDOW_X, WINDOW_Y)
    windows(PEN, WINDOW_X + 50, WINDOW_Y)
    roof(PEN, ROOF_X, ROOF_Y)
    door(PEN, DOOR_X, DOOR_Y)
    done()


if __name__ == "__main__":
    main()