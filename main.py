from framebuffer import clear, drawPolygon, fillPolygon, renderBuffer
from vertex import Vertex2
from color import Color

framebuffer_width = 800
framebuffer_height = 600

clearColor = Color(30, 30, 30)  # Color de fondo
fillColor = Color(0, 255, 0)  # Color de relleno (azul)
borderColor = Color(255, 255, 255)  # Color de la orilla (blanco)
borderWidth = 2  # Grosor de la orilla

def render():
    clear()

    # Definir los vértices del polígono
    vertices = [
        Vertex2(413, 177),
        Vertex2(448, 159),
        Vertex2(502, 88),
        Vertex2(553, 53),
        Vertex2(535, 36),
        Vertex2(676, 37),
        Vertex2(660, 52),
        Vertex2(750, 145),
        Vertex2(761, 179),
        Vertex2(672, 192),
        Vertex2(659, 214),
        Vertex2(615, 214),
        Vertex2(632, 230),
        Vertex2(580, 230),
        Vertex2(597, 215),
        Vertex2(552, 214),
        Vertex2(517, 144),
        Vertex2(466, 180)
    ]

    relleno = [
        Vertex2(682, 175),
        Vertex2(708, 120),
        Vertex2(735, 148),
        Vertex2(739, 170)
    ]
    # Dibujar y rellenar el polígono
    drawPolygon(vertices, fillColor, borderColor, borderWidth)
    fillPolygon(vertices, fillColor)
    fillPolygon(relleno, fillColor)

    # Renderizar el buffer
    renderBuffer()

def main():
    render()

if __name__ == "__main__":
    main()

'''
Poligono 1

Vertex2(165, 380),
Vertex2(185, 360),
Vertex2(180, 330),
Vertex2(207, 345),
Vertex2(233, 330),
Vertex2(230, 360),
Vertex2(250, 380),
Vertex2(220, 385),
Vertex2(205, 410),
Vertex2(193, 383)

Poligono 2

Vertex2(321, 335),
Vertex2(288, 286),
Vertex2(339, 251),
Vertex2(374, 302)

Poligono 3

Vertex2(377, 249),
Vertex2(411, 197),
Vertex2(436, 249)


Poligono 4

Vertex2(413, 177),
Vertex2(448, 159),
Vertex2(502, 88),
Vertex2(553, 53),
Vertex2(535, 36),
Vertex2(676, 37),
Vertex2(660, 52),
Vertex2(750, 145),
Vertex2(761, 179),
Vertex2(672, 192),
Vertex2(659, 214),
Vertex2(615, 214),
Vertex2(632, 230),
Vertex2(580, 230),
Vertex2(597, 215),
Vertex2(552, 214),
Vertex2(517, 144),
Vertex2(466, 180)

Poligono 5

Vertex2(682, 175),
Vertex2(708, 120),
Vertex2(735, 148),
Vertex2(739, 170)
'''