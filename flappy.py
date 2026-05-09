"""El juego flappy, inspirado por flappy bird.

Ejercicios

1. Mantener la puntuación.
2. Variar la velocidad.
3. Variar el tamaño de las pelotas.
4. Permitir que el pajaro se meuva adelante y atras.
"""

from random import randrange
from turtle import (
    clear,
    done,
    dot,
    goto,
    hideturtle,
    onscreenclick,
    ontimer,
    setup,
    tracer,
    up,
    update,
)

from freegames import vector

bird = vector(0, 0)
balls = []


def tap(x, y):
    """Pajaro se mueve arriba en respuesta de un toque a la pantalla."""
    up = vector(0, 30)
    bird.move(up)


def inside(point):
    """regresa true si hay un punto en la pantalla."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Dibuja objetos en la pantalla."""
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'blue')
    else:
        dot(10, 'black')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'red')

    update()


def move():
    """Actualiza la posicion de los objetos."""
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()