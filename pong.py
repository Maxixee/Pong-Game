import turtle

tela = turtle.Screen()
tela.title("PONG feito por @maxixin_")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)

# pontos
score1 = 0
score2 = 0

# player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

# player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.3  # se a bola estiver muito lenta ou muito rapida
bola.dy = 0.3  # basta mudar os valores dessas variaveis


# Placar
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PLAYER 1: 0    PLAYER 2: 0", align="center", font=("Courier", 24, "normal"))


# Funcoes
def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)


def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)


def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)


def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)


# definindo teclado
tela.listen()
tela.onkeypress(player1_up, "w")
tela.listen()
tela.onkeypress(player1_down, "s")
tela.listen()
tela.onkeypress(player2_up, "Up")
tela.listen()
tela.onkeypress(player2_down, "Down")

# loop principal do jogo
while True:
    tela.update()

    # movimentando a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # colisao nas bordas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    elif bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
    elif bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        score1 += 1
        pen.clear()
        pen.write(
            f"PLAYER 1: {score1}    PLAYER 2: {score2}",
            align="center",
            font=("Courier", 24, "normal"),
        )
    elif bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score2 += 1
        pen.clear()
        pen.write(
            f"PLAYER 1: {score1}    PLAYER 2: {score2}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    # colisao nos players
    if (bola.xcor() > 340 and bola.xcor() < 350) and (
        bola.ycor() < player2.ycor() + 40 and bola.ycor() > player2.ycor() - 40
    ):
        bola.setx(340)
        bola.dx *= -1
    elif (bola.xcor() < -340 and bola.xcor() > -350) and (
        bola.ycor() < player1.ycor() + 40 and bola.ycor() > player1.ycor() - 40
    ):
        bola.setx(-340)
        bola.dx *= -1
