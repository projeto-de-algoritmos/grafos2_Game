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
	def ponto_ativo(self):
		mouse_pos = pygame.mouse.get_pos()
		row =  mouse_pos[1] // 32 # Posição exata do mouse na linha
		col =  mouse_pos[0] // 32 # Posição exata do mouse na coluna
		celula_atual = self.matrix[fila][col]
		if celula_atual == 1:
			rect = pygame.Rect((col * 32,fila * 32),(32,32))
			screen.blit(self.select_surf,rect)
	
	def cria_rastro(self):

		# inicio
		inicio_x, inicio_y = self.roomba.sprite.get_coord()
		inicio = self.grid.node(inicio_x,inicio_y)

		# fim
		mouse_pos = pygame.mouse.get_pos()
		fim_x,fim_y =  mouse_pos[0] // 32, mouse_pos[1] // 32
		fim = self.grid.node(fim_x,fim_y)

		# o caminho é recalculado a cada click
		finder = AStarFinder(DiagonalMovement = DiagonalMovement.always)
		self.caminho,_ = finder.find_path(inicio,fim,self.grid)
		self.grid.cleanup()
		
class Game(pygame.sprite.Sprite):
	def _init_(self,sem_caminho):

		# basic
		super()._init_()
		self.image = pygame.image.load('img/roomba.png').convert_alpha()
		self.retangulo = self.image.get_retangulo(center = (60,60))

		# movement
		self.posicao = self.retangulo.center
		self.velocidade = 3
		self.direcao = pygame.math.Vector2(0,0)

		# path
		self.caminho = []
		self.retangulo_colisao = []
		self.sem_caminho = empty_path

	def get_coord(self): #Transforma a posição atual em uma coordenada
		col = self.retangulo.centerx // 32
		row = self.retangulo.centery // 32
		return (col,fila)

	def set_path(self,caminho):
		self.caminho = caminho
		self.cria_colisao_retangulo()
		self.get_direcao()

	def cria_colisao_retangulo(self): # Identificando colisão no mapa
		if self.caminho:
			self.colisao_retangulo = []
			for point in self.path:
				x = (point[0] * 32) + 16
				y = (point[1] * 32) + 16
				retangulo = pygame.Rect((x - 2,y - 2),(4,4))
				self.collision_rects.append(retangulo)

	def get_direction(self):
		if self.collision_rects:
			inicio = pygame.math.Vector2(self.pos)
			fim = pygame.math.Vector2(self.collision_rects[0].center)
			self.direcao = (fim - inicio).normalize()
		else:
			self.direcao = pygame.math.Vector2(0,0)
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

