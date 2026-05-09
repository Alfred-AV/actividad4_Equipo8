"""Pong, juego clásico de arcade.

Ejercicios

1. Cambia los colores.
2. ¿Cuál es la velocidad de cuadros? Hazlo más rápido o más lento.
3. Cambia la velocidad de la pelota.
4. Cambia el tamaño de las paletas.
5. Cambia cómo rebota la pelota en las paredes.
6. ¿Cómo agregarías un jugador controlado por la computadora?
7. Agrega una segunda pelota.
"""

from random import choice, random
from turtle import (
    up,
    goto,
    down,
    begin_fill,
    forward,
    left,
    end_fill,
    clear,
    color,
    dot,
    update,
    ontimer,
    setup,
    bgcolor,
    hideturtle,
    tracer,
    listen,
    onkey,
    done,
)

from freegames import vector


def value():
    """Genera aleatoriamente un valor entre (-5, -3) o (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}


def move(player, change):
    """Mueve la posición del jugador según el cambio indicado."""
    state[player] += change


def rectangle(x, y, width, height):
    """Dibuja un rectángulo en (x, y) con el ancho y alto dados."""
    up()
    goto(x, y)
    down()
    begin_fill()

    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()


def draw():
    """Dibuja el juego y mueve la pelota."""
    clear()

    # Rectángulos blancos
    color("white")
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    # Pelota roja
    up()
    goto(x, y)
    dot(10, "red")
    update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    ontimer(draw, 50)


setup(420, 420, 370, 0)

# Fondo negro
bgcolor("black")

hideturtle()
tracer(False)
listen()

onkey(lambda: move(1, 20), "w")
onkey(lambda: move(1, -20), "s")
onkey(lambda: move(2, 20), "i")
onkey(lambda: move(2, -20), "k")

draw()
done()
