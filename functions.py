from graphics import *
from math import *

#Funções acrescentadas na biblioteca

#calcula a distância entre dois pontos
def calculate_points_distance(p1, p2):
    return sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)

#calcula a área de um triângulo dados 3 pontos
def calculate_triangle_area(p1, p2, p3):
    x1, y1 = (p2.getX() - p1.getX(), p2.getY() - p1.getY())
    x2, y2 = (p3.getX() - p1.getX(), p3.getY() - p1.getY())
    
    determinant = x1 * y2 - x2 * y1

    return abs(determinant) / 2

#calcula produto escalar entre dois vetores
def calculate_dot_product(p1, p2):
    return p1.getX() * p2.getX() + p1.getY() * p2.getY()

#verifica ponto/click dentro de um círculo
def verify_inside_point(circle, point):
    distance = calculate_points_distance(circle.getCenter(), point)
    if distance <= circle.getRadius():
        return True
    return False

#verifica colisão entre dois círculos
def verify_colision_circles(circle, circle_2):
    centers_distance = calculate_points_distance(circle.getCenter(), circle_2.getCenter())
    if centers_distance <= circle.getRadius() + circle_2.getRadius():
        return True
    return False

#verifica se um círculo está completamente dentro do outro
def verify_inside_circle(circle, circle_2):
    centers_distance = calculate_points_distance(circle.getCenter(), circle_2.getCenter())
    if centers_distance <= abs(circle.getRadius() - circle_2.getRadius()):
        return True
    return False

#verifica colisão entre círculo e retângulo (Não é eficiente, mas pode ser instrutiva)
def verify_colision_circle_rectangle(circle, rectangle):    
    for i in range(360):
        x = circle.getCenter().getX() + circle.getRadius() * cos(i * (pi / 180))
        y = circle.getCenter().getY() - circle.getRadius() * sin(i * (pi / 180))
        if x >= rectangle.getP1().getX() and x <= rectangle.getP2().getX():  
            if y >= rectangle.getP1().getY() and y <= rectangle.getP2().getY():
                return True
    return False

#verifica colisão entre círculo e retângulo (Eficiente)
def verify_colision_circle_rectangle2(circle, rectangle):
    p1 = rectangle.getP1()
    p2 = rectangle.getP2()

    polygon = Polygon(Point(p1.getX(), p1.getY()), Point(p2.getX(), p1.getY()), Point(p2.getX(), p2.getY()), Point(p1.getX(), p2.getY()))
    if verify_colision_circle_polygon(circle, polygon):
        return True
    return False

#verifica colisão entre círculo e linha
def verify_colision_circle_line(circle, line):
    center = circle.getCenter()
    p1 = line.getP1()
    p2 = line.getP2()

    distance_1 = calculate_points_distance(center, p1)
    distance_2 = calculate_points_distance(center, p2)
    max_distance = distance_1 if distance_1 > distance_2 else distance_2
    
    dot_product_1 = calculate_dot_product(Point(p1.getX() - center.getX(), p1.getY() - center.getY()), Point(p1.getX() - p2.getX(), p1.getY() - p2.getY()))
    dot_product_2 = calculate_dot_product(Point(p2.getX() - center.getX(), p2.getY() - center.getY()), Point(p2.getX() - p1.getX(), p2.getY() - p1.getY()))

    if dot_product_1 > 0 and dot_product_2 > 0:
        triangle_area = calculate_triangle_area(center, p1, p2)
        points_distance = calculate_points_distance(p1, p2)
        min_distance = 2 * triangle_area / points_distance
    else:
        min_distance = distance_1 if distance_1 < distance_2 else distance_2
        
    if min_distance <= circle.getRadius() and max_distance >= circle.getRadius():
        return True
    return False

#verifica colisão entre círculo e polígono
def verify_colision_circle_polygon(circle, polygon):
    points = polygon.getPoints()
    for i in range(len(points)):
        point_1 = points[i]
        point_2 = points[(i + 1) % len(points)]
        if verify_colision_circle_line(circle, Line(point_1, point_2)):
            return True
    return False
