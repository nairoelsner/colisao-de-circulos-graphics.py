from graphics_modificada import *
from math import *

win = GraphWin("Colisão de círculos", 300, 250, autoflush = False)

circle = Circle(Point(150, 100), 20)
circle.setWidth(2)
circle.draw(win)

circle_2 = Circle(Point(50, 125), 30)
circle_2.setOutline("red")
circle_2.setWidth(2)
circle_2.draw(win)

square = Rectangle(Point(225, 100), Point(275, 150))
square.setOutline("blue")
square.setWidth(2)
square.draw(win)

polygon = Polygon(Point(150, 20), Point(130, 50), Point(170, 50), Point(110, 70), Point(100, 30))
polygon.setOutline("green")
polygon.setWidth(2)
polygon.draw(win)

line = Line(Point(130, 160), Point(180, 200))
line.setFill("orange")
line.setWidth(2)
line.draw(win)

triangle = Polygon(circle.getCenter(), Point(circle.getCenter().getX(), circle_2.getCenter().getY()), circle_2.getCenter())
triangle.setOutline("red")
triangle.setWidth(2)
triangle.draw(win)

triangle_2 = Polygon(circle.getCenter(), line.getP1(), line.getP2())
triangle_2.setOutline("orange3")
triangle_2.setWidth(2)
triangle_2.draw(win)

message = Text(Point(150, 230), 'Não há colisão')
message.draw(win)

circunference_triangle = Point(0, 0)
i = 0
while True:
    key = win.checkKey()
    click = win.checkMouse()

    #movimentos do círculo
    if key == "Up":
        circle.move(0, -5)
    elif key == "Down":
        circle.move(0, 5)
    elif key == "Left":
        circle.move(-5, 0)
    elif key == "Right":
        circle.move(5, 0)

    messageText = 'Não há colisão'

    #verificações de colisão
    if circle.verify_colision(click):
        print("click dentro do círculo")
    
    if circle.verify_colision(line):
        messageText = 'Colisão com linha'
        print("colisão com linha")
    
    if circle.verify_colision(square):
        messageText = 'Colisão com quadrado'
        print("colisão com quadrado")
    
    if circle.verify_colision(polygon):
        messageText = 'Colisão com polígono'
        print("colisão com polígono")

    if circle.verify_colision(circle_2):
        messageText = 'Colisão com círculo'
        print("colisão com círculo")
    
    if circle.verify_inside_circle(circle_2):
        messageText = 'Círculo interno'
        print("círculo interno")
    
    message.setText(messageText)
    
    #animações para ilustrar os algoritmos
    if key in ["Up", "Down", "Left", "Right"]:
        triangle.undraw()
        triangle = Polygon(circle.getCenter(), Point(circle.getCenter().getX(), circle_2.getCenter().getY()), circle_2.getCenter())
        triangle.setOutline("red")
        triangle.setWidth(2)
        triangle.draw(win)

        line.undraw()
        triangle_2.undraw()
        triangle_2 = Polygon(circle.getCenter(), line.getP1(), line.getP2())
        triangle_2.setOutline("orange3")
        triangle_2.setWidth(2)
        triangle_2.draw(win)
        line.draw(win)
    
    circunference_triangle.undraw()
    circunference_x = circle.getCenter().getX() + circle.getRadius() * cos(i * (pi / 180))
    circunference_y = circle.getCenter().getY() - circle.getRadius() * sin(i * (pi / 180))
    circunference_triangle = Polygon(circle.getCenter(), Point(circunference_x, circle.getCenter().getY()), Point(circunference_x, circunference_y))
    circunference_triangle.setOutline("blue")
    circunference_triangle.setWidth(2)
    circunference_triangle.draw(win)
    i += 1
    
    if i > 359:
        i = 0
    update(180)