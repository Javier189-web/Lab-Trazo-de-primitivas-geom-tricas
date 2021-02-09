import pygame,sys
from pygame.locals import *
from tkinter import *


pygame.init()
ventana = pygame.display.set_mode((700,700))
pygame.display.set_caption("Figuras Geometricas")

pygame.draw.circle(ventana, (80,70,120), (80,90), 20)
pygame.draw.rect(ventana, (130,70,70), (0,0,100,50))
pygame.draw.polygon(ventana,(90,180,70),((300,0),(400,106),(350,230),(250,230),(200,106)))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()