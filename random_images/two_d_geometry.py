import pygame
try:
    from . import temp_file
except:
    import temp_file
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

def triangles(width, height, tri_count=random.randint(2,30), line_widths=range(0,12),
        fg_color_fn=lambda: pygame.Color(*(int(i*255) for i in colorsys.hsv_to_rgb(random.random(),random.random(),1))),
        bg_color=pygame.Color(random.randint(0,128), random.randint(0,128), random.randint(0,128))):
    surface = pygame.Surface((width, height))
    surface.fill(pygame.Color(*bg_color))
    for i in range(tri_count):
        verts = [(random.randint(0,width), random.randint(0,height)) for n in range(3)]
        pygame.draw.polygon(surface, pygame.Color(*fg_color_fn()), verts, random.choice(list(line_widths)+[0]*4))
    path = temp_file.TemporaryFile.generate_new('png')
    pygame.image.save(surface, path)
    return path


def circles(width, height, circ_count=random.randint(2,30), circ_radii=range(25,200), line_widths=range(0,12),
        fg_color_fn=lambda: pygame.Color(*(int(i*255) for i in colorsys.hsv_to_rgb(random.random(),random.random(),1))),
        bg_color=pygame.Color(random.randint(0,128), random.randint(0,128), random.randint(0,128))):
    surface = pygame.Surface((width, height))
    surface.fill(pygame.Color(*bg_color))
    for i in range(circ_count):
        pygame.draw.circle(surface, pygame.Color(*fg_color_fn()),
                (random.randint(0,width), random.randint(0,height)),
                random.choice(circ_radii),
                random.choice(list(line_widths)+[0]*(len(line_widths)//5)))
    path = temp_file.TemporaryFile.generate_new('png')
    pygame.image.save(surface, path)
    return path

if __name__=='__main__':
    print(circles(512,512).persist())
