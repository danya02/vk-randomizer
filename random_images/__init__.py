from . import perlin_noise
import random
import colorsys

width=512
height=512

def mono_perlin_noise():
    if random.random()>0.4:
        bg_color = (0,0,0)
        fg_color = [int(i*255) for i in colorsys.hsv_to_rgb(random.random(),1,1)]
    else:
        hue = random.random()
        other_hue = 0.5+hue
        if other_hue>1:other_hue -= 1
        fg_color = [int(i*255) for i in colorsys.hsv_to_rgb(hue,1,1)]
        bg_color = [int(i*255) for i in colorsys.hsv_to_rgb(other_hue,1,1)]
    step = random.random()/5
    return perlin_noise.generate_monochrome(width,height,fg_color=fg_color,bg_color=bg_color,
            px_step=lambda x:x+step, py_step=lambda y:y+step, octaves=random.randint(1,7))

def colorful_perlin_noise():
    bg_color=(255,255,255)
    fg_color=(0,0,0)
    if random.random()>0.5:
        bg_color,fg_color = fg_color, bg_color

    step=random.random()/5
    return perlin_noise.generate_colorful(width,height,fg_color=fg_color,bg_color=bg_color,
            px_step=lambda x:x+step, py_step=lambda y:y+step, octaves=random.randint(1,7))
    

def get_any():
    actions = [mono_perlin_noise, colorful_perlin_noise]
    return random.choice(actions)()
