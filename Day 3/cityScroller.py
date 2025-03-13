# Name: Dia Yamamoto
# Purpose: we're gonna use the pygame library to create a backdrop of buildings that are all of random heights. 

import pygame 
import random 

# creating variables for each of the colors
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (235,153,40)

#init aka initialize the pygame
pygame.init()

# set the width and height of the screen 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# set the title of the pygame screen 
pygame.display.set_caption("City Scroller")

# game logic loop to prevent game end until window is closed. 
done = False

# how fast the screen will update
clock = pygame.time.Clock()

# create Building class
class Building():
  def __init__(self, x_point, y_point, width, height, color):
    self.x_point = x_point
    self.y_point = y_point
    self.width = width
    self.height = height
    self.color = color 

  def Draw(self):
    pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

  def move(self, speed):
    self.x_point -= speed


class Scroller(object): 
  def __init__(self, width, height, base, color, speed):
    self.width = width
    self.height = height
    self.base = base
    self.color = color
    self.speed = speed
    self.building_list = []
    self.add_buildings()

  def add_building(self, x_location):
    building_height = random.randint(100, self.height)
    building_width = random.randint(50,175)
    self.building_list.append(Building(x_location, SCREEN_HEIGHT -building_height, building_width, building_height, self.color))

  def add_buildings(self):
    unfilled_width = 0 
    while unfilled_width < 800: 
      self.add_building(700-unfilled_width)
      unfilled_width += self.building_list[-1].width
    
    
