from framebuffer import clear, drawPolygon, fillPolygon, renderBuffer
from vertex import Vertex2
from color import Color

framebuffer_width = 800
framebuffer_height = 600

clearColor = Color(30, 30, 30)  # Color de fondo
fillColor = Color(70, 130, 180)  # Color de relleno (azul)
borderColor = Color(255, 255, 255)  # Color de la orilla (blanco)
borderWidth = 2  # Grosor de la orilla

def render():
    clear()

    # Definir los vértices del polígono
    vertices = [
        Vertex2(321, 335),
        Vertex2(288, 286),
        Vertex2(339, 251),
        Vertex2(374, 302)
    ]

    # Dibujar y rellenar el polígono
    drawPolygon(vertices, fillColor, borderColor, borderWidth)
    fillPolygon(vertices, fillColor)

    # Renderizar el buffer
    renderBuffer()

def main():
    render()

if __name__ == "__main__":
    main()
