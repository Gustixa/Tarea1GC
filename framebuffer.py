from color import Color
from vertex import Vertex2

framebuffer_width = 800
framebuffer_height = 600

framebuffer = [Color(0, 0, 0)] * (framebuffer_width * framebuffer_height)

clearColor = Color(0, 0, 0)  # Color de fondo

def clear():
    global framebuffer
    framebuffer = [clearColor] * (framebuffer_width * framebuffer_height)

def point(vertex, color):
    global framebuffer
    x = int(vertex.x)
    y = int(vertex.y)
    if 0 <= x < framebuffer_width and 0 <= y < framebuffer_height:
        framebuffer[y * framebuffer_width + x] = color

def line(x0, y0, x1, y1, color, width):
    # Verificar si los puntos iniciales y finales están dentro de los límites del framebuffer
    if x0 < 0 or x0 >= framebuffer_width or y0 < 0 or y0 >= framebuffer_height or x1 < 0 or x1 >= framebuffer_width or y1 < 0 or y1 >= framebuffer_height:
        return

    # Convertir los valores iniciales y finales a enteros
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy

    while True:
        point(Vertex2(x0, y0), color if isBorder(x0, y0, x1, y1, width) else clearColor)

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def isBorder(x, y, x0, y0, width):
    dx = abs(x - x0)
    dy = abs(y - y0)
    return dx <= width or dy <= width

def drawPolygon(vertices, fillColor, borderColor, borderWidth):
    for i in range(len(vertices)):
        current_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % len(vertices)]  # El operador % asegura que volvamos al primer vértice al final del array

        line(current_vertex.x, current_vertex.y, next_vertex.x, next_vertex.y, borderColor, borderWidth)

    # Dibujar la última línea que cierra el polígono
    last_vertex = vertices[-1]
    first_vertex = vertices[0]
    line(last_vertex.x, last_vertex.y, first_vertex.x, first_vertex.y, borderColor, borderWidth)

def fillPolygon(vertices, fillColor):
    min_x = min(vertices, key=lambda v: v.x).x
    max_x = max(vertices, key=lambda v: v.x).x
    min_y = int(min(vertices, key=lambda v: v.y).y)
    max_y = int(max(vertices, key=lambda v: v.y).y)

    for y in range(min_y, max_y + 1):
        intersections = []

        for i in range(len(vertices)):
            current_vertex = vertices[i]
            next_vertex = vertices[(i + 1) % len(vertices)]

            if (current_vertex.y <= y < next_vertex.y) or (current_vertex.y >= y > next_vertex.y):
                intersection_x = current_vertex.x + ((y - current_vertex.y) / (next_vertex.y - current_vertex.y)) * (next_vertex.x - current_vertex.x)
                intersections.append(intersection_x)

        intersections.sort()

        for i in range(0, len(intersections), 2):
            start_x = int(intersections[i])
            end_x = int(intersections[i + 1]) if i + 1 < len(intersections) else start_x

            for x in range(start_x, end_x + 1):
                point(Vertex2(x, y), fillColor)


def renderBuffer():
    global framebuffer

    # Definir el encabezado del archivo BMP
    file_size = 14 + 40 + (framebuffer_width * framebuffer_height * 3)  # Tamaño total del archivo
    reserved = 0  # Reservado, debe ser 0
    offset = 54  # Offset de los datos de píxeles
    dib_header_size = 40  # Tamaño del encabezado DIB (info del bitmap)
    image_width = framebuffer_width  # Ancho de la imagen
    image_height = framebuffer_height  # Alto de la imagen
    planes = 1  # Número de planos, debe ser 1
    bits_per_pixel = 24  # Bits por píxel (RGB de 24 bits)
    compression = 0  # Compresión, 0 para sin compresión
    image_size = framebuffer_width * framebuffer_height * 3  # Tamaño de los datos de píxeles
    x_resolution = 0  # Resolución horizontal en píxeles por metro
    y_resolution = 0  # Resolución vertical en píxeles por metro
    colors = 0  # Número de colores en la paleta, 0 para paleta completa
    important_colors = 0  # Número de colores importantes, 0 para todos

    with open('poligono-1.bmp', 'wb') as f:
        f.write(b'BM')
        f.write(file_size.to_bytes(4, 'little'))
        f.write(reserved.to_bytes(4, 'little'))
        f.write(offset.to_bytes(4, 'little'))
        f.write(dib_header_size.to_bytes(4, 'little'))
        f.write(image_width.to_bytes(4, 'little'))
        f.write(image_height.to_bytes(4, 'little'))
        f.write(planes.to_bytes(2, 'little'))
        f.write(bits_per_pixel.to_bytes(2, 'little'))
        f.write(compression.to_bytes(4, 'little'))
        f.write(image_size.to_bytes(4, 'little'))
        f.write(x_resolution.to_bytes(4, 'little'))
        f.write(y_resolution.to_bytes(4, 'little'))
        f.write(colors.to_bytes(4, 'little'))
        f.write(important_colors.to_bytes(4, 'little'))

        for y in range(framebuffer_height - 1, -1, -1):
            for x in range(framebuffer_width):
                pixel = framebuffer[y * framebuffer_width + x]
                f.write(pixel.b.to_bytes(1, 'little'))
                f.write(pixel.g.to_bytes(1, 'little'))
                f.write(pixel.r.to_bytes(1, 'little'))
