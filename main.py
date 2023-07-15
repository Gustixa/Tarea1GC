from color import Color
from vertex import Vertex2
from framebuffer import clear, drawPolygon, fillPolygon, renderBuffer

framebuffer_width = 800
framebuffer_height = 600

framebuffer = [Color(0, 0, 0)] * (framebuffer_width * framebuffer_height)

clearColor = Color(0, 0, 0)  # Color de fondo
currentColor = Color(255, 255, 255)  # Color actual

def render():
    clear()

    # Definir los vértices del polígono
    vertices = [
        Vertex2(100, 100),
        Vertex2(200, 200),
        Vertex2(200, 400),
        Vertex2(300, 300),
        Vertex2(400, 400),
        Vertex2(400, 200)
    ]

    # Dibujar el polígono
    drawPolygon(vertices)

    # Rellenar el polígono
    fillPolygon(vertices)

    # Renderizar el buffer
    renderBuffer()

def main():
    render()

if __name__ == "__main__":
    main()
