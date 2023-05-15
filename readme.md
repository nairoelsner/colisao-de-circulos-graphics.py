
# Módulo de colisões entre círculos e formas geométricas para graphics.py

## Objetivo
Este projeto consiste em um conjunto de funções desenvolvidas para facilitar o cálculo de colisões entre círculos e outras formas geométricas, de forma performática, utilizando a biblioteca graphics.py. As funções fornecidas permitem verificar colisões entre um círculo e outros círculos, pontos, retângulos, linhas e polígonos. Os conceitos matemáticos podem ser aplicados podem ser aplicados em qualquer outra biblioteca de sua preferência.


## Utilização
Coloque o arquivo graphics_modificada.py no diretório do seu projeto e importe no seu código.
````python
from graphics_modificada import *
````


## Exemplos de Uso

- ### Verificar colisão entre dois círculos:
````python
from graphics_modificada import *

#Criação dos círculos
circle1 = Circle(Point(100, 100), 50)
circle2 = Circle(Point(150, 150), 30)

#Verificar colisão
if circle1.verify_colision(circle2):
	print("Colisão detectada entre circle1 e circle2")
else:
	print("Não há colisão entre circle1 e circle2")
````

- ### Verificar se um ponto está dentro de um círculo:
````python
from graphics_modificada import *

#Criação do círculo
circle = Circle(Point(100, 100), 50) 

#Criação do ponto
point = Point(120, 120)

#Verificar se o ponto está dentro do círculo
if circle.verify_colision(point):
	print("O ponto está dentro do círculo")
else:
	print("O ponto está fora do círculo")
````

- ### Verificar colisão entre um círculo e um retângulo:
````python
from graphics_modificada import *

#Criação do círculo
circle = Circle(Point(100, 100), 50)

#Criação do retângulo
rectangle = Rectangle(Point(80, 80), Point(120, 120))

#Verificar colisão entre o círculo e o retângulo
if circle.verify_colision(rectangle):
	print("Colisão detectada entre o círculo e o retângulo")
else:
	print("Não há colisão entre o círculo e o retângulo")
````

- ### Verificar colisão entre um círculo e um polígono:

````python
from graphics_modificada import *

#Criação do círculo
circle = Circle(Point(100, 100), 50)

#Criação dos pontos do polígono
p1 = Point(120, 120)
p2 = Point(150, 150)
p3 = Point(120, 180)
p4 = Point(80, 160)
polygon = Polygon(p1, p2, p3, p4)

#Verificar colisão entre o círculo e o polígono
if circle.verify_colision(polygon):
	print("Colisão detectada entre o círculo e o polígono")
else:
	print("Não há colisão entre o círculo e o polígono")
````

- ### Verificar colisão entre um círculo e uma linha:
````python
from graphics_modificada import *

#Criação do círculo
circle = Circle(Point(100, 100), 50)

#Criação dos pontos da linha
p1 = Point(80, 80)
p2 = Point(120, 120)
line = Line(p1, p2)

#Verificar colisão entre o círculo e a linha
if circle.verify_colision(line):
	print("Colisão detectada entre o círculo e a linha")
else:
	print("Não há colisão entre o círculo e a linha"
````


## Funções Disponíveis
 Para fins pedagógicos, você encontrará uma demonstração de utilização no arquivo main.py e as funções inseridas na biblioteca no arquivo functions.py. 

Aqui está uma breve descrição das principais funções disponíveis neste conjunto:

**calculate_points_distance(p1, p2):** Calcula a distância entre dois pontos.

**calculate_triangle_area(p1, p2, p3):** Calcula a área de um triângulo dado três pontos.

**calculate_dot_product(p1, p2):** Calcula o produto escalar entre dois vetores.

**verify_inside_click(click):** Verifica se um ponto está dentro do círculo.

**verify_colision_circles(circle):** Verifica a colisão entre dois círculos.

**verify_inside_circle(circle):** Verifica se um círculo está completamente dentro do outro.

**verify_colision_circle_rectangle(rectangle):** Verifica a colisão entre um círculo e um retângulo.

**verify_colision_circle_line(line):** Verifica a colisão entre um círculo e uma linha.

**verify_colision_circle_polygon(polygon):** Verifica a colisão entre um círculo e um polígono.


## Considerações Finais
O projeto fornece um conjunto de funções úteis para facilitar a detecção de colisões entre círculos e outras formas geométricas em aplicações gráficas que utilizam a biblioteca graphics.py. Essas funções podem ser incorporadas em projetos que envolvam jogos, simulações e outras aplicações interativas que exigem cálculos de colisão entre círculos. Espero que esse conjunto de funções simplifique seu processo de desenvolvimento e torne mais fácil implementar a lógica de colisão em seus projetos.
