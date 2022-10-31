import pygame
import sys
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("pygame")
width = 40
height= 60
x = 50
y = 50
velocity = 5


run = True
while run:
  pygame.time.delay(100)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
      
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_LEFT]:
    x -= velocity
  if keys[pygame.K_RIGHT]:
    x += velocity
  if keys[pygame.K_UP]:
    y -= velocity
  if keys[pygame.K_DOWN]:
    y += velocity
  
  win.fill((0,0,0))
  pygame.draw.rect(win,(255,0,0), (x,y,width,height))
  pygame.display.update()