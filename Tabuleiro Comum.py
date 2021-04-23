import turtle
def quadrado(posx, posy, lado, cor):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.fillcolor(cor)
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    turtle.end_fill()
    turtle.hideturtle()

def tabuleiro(posx, posy, lado, n, cor_1, cor_2):
    #Desenha um tabuleiro de xadrez.
    for i in range(n):
        # desenha linha n
        # -- posiciona
        turtle.penup()
        turtle.goto(posx, i * lado)
        turtle.pendown()

        # --- escolhe cor
        if i % 2 == 0:
            primo = cor_1
            segundo = cor_2
        else:
            primo = cor_2
            segundo = cor_1

        # --- desenha
        for j in range(n):
            if j % 2 == 0:
                # desenha quadrado j
                quadrado(turtle.xcor(), turtle.ycor(), lado, primo)
            else:
                quadrado(turtle.xcor(), turtle.ycor(), lado, segundo)
                # posiciona
                turtle.penup()
                turtle.setx(turtle.xcor() + lado)
                turtle.pendown()

if __name__ == '__main__':
    tabuleiro(-100, -100, 40, 6, 'white', 'black')
    turtle.exitonclick()