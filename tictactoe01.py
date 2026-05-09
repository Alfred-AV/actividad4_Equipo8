"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
from turtle import *
from freegames import line

def grid():
    """Dibuja la cuadrícula base del juego."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Dibuja la X en color rojo y con trazo grueso."""
    color('red') # Define el color del trazo
    width(10)    # Define el grosor de la línea
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)

def drawo(x, y):
    """Dibuja el O en color azul y con trazo grueso."""
    color('blue') # Define el color del trazo
    width(10)     # Define el grosor de la línea
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)

def floor(value):
    """Alinea el clic a la cuadrícula (celdas de 133px)."""
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    """Lógica principal al hacer clic en la pantalla."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    # Cambia el turno: si es 0 pasa a 1, y viceversa
    state['player'] = not player

# Configuración de ventana y ejecución
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
