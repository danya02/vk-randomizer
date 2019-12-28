import pygame
from . import temp_file
import random
import colorsys

def straight_lines_color(width, height, line_count=random.randint(3,50)):
    surface = pygame.Surface((width, height))
    surface.fill(pygame.Color(random.randint(0,200), random.randint(0,200), random.randint(0,200)))
    for i in range(line_count):
        start = (random.randint(0,width), random.randint(0,height))
        end = (random.randint(0,width), random.randint(0,height))
        color = pygame.Color(*[int(i*255) for i in colorsys.hsv_to_rgb(random.random(),1,1)])
        line_width = random.randint(1,10)
        pygame.draw.line(surface, color, start, end, line_width)
    path = temp_file.TemporaryFile.generate_new('png')
    pygame.image.save(surface, path)
    return path

def straight_lines_mono(width, height, line_count=random.randint(3,50),
        bg_color=(0,0,0),
        fg_color=(int(i*255) for i in colorsys.hsv_to_rgb(random.random(),random.random(),1))):
    surface = pygame.Surface((width, height))
    surface.fill(pygame.Color(*bg_color))
    fg_color = pygame.Color(*fg_color)
    for i in range(line_count):
        start = (random.randint(0,width), random.randint(0,height))
        end = (random.randint(0,width), random.randint(0,height))
        line_width = random.randint(1,10)
        pygame.draw.line(surface, fg_color, start, end, line_width)
    path = temp_file.TemporaryFile.generate_new('png')
    pygame.image.save(surface, path)
    return path

if __name__=='__main__':
    print(straight_lines_mono(512,512).persist())
