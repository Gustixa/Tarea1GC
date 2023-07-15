from color import Color
from vertex import Vertex2
from framebuffer import clear, drawPolygon, fillPolygon, renderBuffer

framebuffer_width = 800
framebuffer_height = 600

framebuffer = [Color(0, 0, 0)] * (framebuffer_width * framebuffer_height)

clearColor = Color(0, 0, 0)  # Color de fondo
fillColor = Color(255, 165, 0)  # Color de relleno
borderColor = Color(255, 255, 255)  # Color de la orilla

def render():
    clear()

    # Definir los vértices del polígono
    vertices = [
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
    ]

    # Dibujar y rellenar el polígono con un grosor de orilla de 2 píxeles
    drawPolygon(vertices, fillColor, borderColor, 60)
    fillPolygon(vertices, fillColor)

    # Renderizar el buffer
    renderBuffer()

def main():
    render()

if __name__ == "__main__":
    main()
