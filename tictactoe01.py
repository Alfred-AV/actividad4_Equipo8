"""Tic Tac Toe - Versión corregida para flake8."""

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

import turtle
from freegames import line


def grid():
    """Dibuja la cuadrícula base del juego."""
    turtle.width(3)
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja la X en color rojo."""
    turtle.color('red')  # Dos espacios antes del comentario
    turtle.width(10)
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)


def drawo(x, y):
    """Dibuja el O en color azul."""
    turtle.color('blue')  # Color del círculo
    turtle.width(10)
    turtle.up()
    turtle.goto(x + 67, y + 5)
    turtle.down()
    turtle.circle(62)


def floor(value):
    """Alinea el clic a la cuadrícula."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Lógica principal al hacer clic."""
    x_coord = floor(x)
    y_coord = floor(y)
    player = state['player']
    draw = players[player]
    draw(x_coord, y_coord)
    turtle.update()
    state['player'] = not player


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
