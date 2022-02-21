import pygame, sys
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

pygame.init()
screen = pygame.display.set_mode((1280,736))
clock = pygame.time.Clock()
class caminho:
	def __init__(self,matriz):

		# base
		self.matriz = matriz
		self.grid = Grid(matrix = matriz)
		self.select_surf = pygame.image.load('img/mouse.png').convert_alpha()

		# caminho
		self.caminho = []



bg_surf = pygame.image.load('img/map.jpg').convert()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.blit(bg_surf, (0, 0))
	pygame.display.update()
	clock.tick(60)

