# Name: Dia Yamamoto
# Purpose: let's code a snow storm to cool off 

import pygame
import random 

# define some colors 
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

# set width and height of screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# snowflake class
class Snowflake():
  def __init__(self, snowsize, x, y, speed):
    self.snowsize = snowsize
    self.x = x
    self.y = y
    self.speed = speed

  def fall(self,screen):
    # changes y location of snow each time it falls
    self.y += self.speed
    # check if snow is still on screen
    if self.y >= 500:  
      # send snowflake back to the top
      self.y = 10
    # draw a snowflake
    pygame.draw.circle(screen,WHITE,[self.x,self.y], self.snowsize)

# check whether the user clicks the close button or not
done = False

# used to manage how fast the screen updates
clock = pygame.time.Clock()

# speed of snowfall
speed = 3

# a list that will contain all of our snowflakes! 
snow_list = []

# ----- Main Code -----
while not done:
  for event in  pygame.event.get():
      if event.type == pygame.QUIT:
        done = True

  for i in range(8):
    snow_list.append(Snowflake(random.randint(1,3), random.randint(0,700),0, speed))
  
  screen.fill(BLACK)

  # tell snowflakes to fall
  for snowflake in snow_list:
    snowflake.fall(screen)

  # updates the screen with what we've drawn
  pygame.display.flip()

  clock.tick(60)

#closes the window and quits
pygame.quit()
exit()




  
