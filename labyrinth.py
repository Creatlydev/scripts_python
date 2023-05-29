import pygame
import random

# Tamaño de cada celda del laberinto
CELL_SIZE = 20

# Ancho y alto del laberinto (en celdas)
WIDTH = 30
HEIGHT = 20

# Ancho y alto de la pantalla (en pixels)
SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Diccionario para almacenar los vecinos de cada celda
neighbors = {}

# Inicializa Pygame
pygame.init()

# Establece el tamaño de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clase para representar una celda del laberinto


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = [True, True, True, True]  # top, right, bottom, left

# Función para dibujar una celda del laberinto


def draw_cell(cell):
    x = cell.x * CELL_SIZE
    y = cell.y * CELL_SIZE
    if cell.walls[0]:
        pygame.draw.line(screen, WHITE, (x, y), (x + CELL_SIZE, y), 1)
    if cell.walls[1]:
        pygame.draw.line(screen, WHITE, (x + CELL_SIZE, y),
                         (x + CELL_SIZE, y + CELL_SIZE), 1)
    if cell.walls[2]:
        pygame.draw.line(screen, WHITE, (x + CELL_SIZE, y +
                         CELL_SIZE), (x, y + CELL_SIZE), 1)
    if cell.walls[3]:
        pygame.draw.line(screen, WHITE, (x, y + CELL_SIZE), (x, y), 1)


# Crea una matriz de celdas para representar el laberinto
grid = [[Cell(x, y) for y in range(HEIGHT)] for x in range(WIDTH)]

# Calcula los vecinos de cada celda
for x in range(WIDTH):
    for y in range(HEIGHT):
        neighbors[(x, y)] = []
        if x > 0:
            neighbors[(x, y)].append((x - 1, y))
        if x < WIDTH - 1:
            neighbors[(x, y)].append((x + 1, y))
        if y > 0:
            neighbors[(x, y)].append((x, y - 1))
        if y < HEIGHT - 1:
            neighbors[(x, y)].append((x, y + 1))


# Función para remover los muros entre dos celdas vecinas
def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls[3] = False
        next.walls[1] = False
    elif dx == -1:
        current.walls[1] = False
        next.walls[3] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls[0] = False
        next.walls[2] = False
    elif dy == -1:
        current.walls[2] = False
        next.walls[0] = False

# Función para generar el laberinto utilizando el algoritmo de la espalda


def generate_maze():
    stack = []
    current = grid[0][0]
    current.visited = True
    stack.append(current)
    while stack:
        current = stack[-1]
        neighbors_list = neighbors[(current.x, current.y)]
        neighbors_list = [
            n for n in neighbors_list if not grid[n[0]][n[1]].visited]
        if neighbors_list:
            next = random.choice(neighbors_list)
            next = grid[next[0]][next[1]]
            remove_walls(current, next)
            next.visited = True
            stack.append(next)
        else:
            stack.pop()


# Función para encontrar el camino a través del laberinto
def find_path():
    # Crea una copia del laberinto para marcar las celdas visitadas
    visited = [[cell.visited for cell in row] for row in grid]
    visited[0][0] = True

    # Lista de celdas por visitar
    queue = [(0, 0)]

    # Diccionario para almacenar la ubicación anterior de cada celda
    prev = {}

    # Bandera para indicar si se ha encontrado la salida
    found = False

    # Bucle hasta que se haya encontrado la salida o no queden celdas por visitar
    while queue and not found:
        x, y = queue.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            # Revisa si la celda adyacente está dentro del laberinto y no ha sido visitada
            if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT and not visited[x + dx][y + dy]:
                # Marca la celda como visitada y la agrega a la lista
                visited[x + dx][y + dy] = True
                queue.append((x + dx, y + dy))
                # Almacena la ubicación anterior de la celda
                prev[(x + dx, y + dy)] = (x, y)
                # Si la celda es la salida, establece la bandera
                if x + dx == WIDTH - 1 and y + dy == HEIGHT - 1:
                    found = True
                    break

    # Si se encontró la salida, dibuja el camino desde la salida hasta la entrada
    if found:
        x, y = WIDTH - 1, HEIGHT - 1
        while x != 0 or y != 0:
            pygame.draw.rect(screen, BLUE, (x * CELL_SIZE,
                             y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            x, y = prev[(x, y)]


# Genera el laberinto
generate_maze()


find_path()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            draw_cell(grid[x][y])
    find_path()
    pygame.display.flip()

pygame.quit()
