import random
import subprocess
import os
import colorsys

# ===== BEGIN block to import pygame =====
import sys
null = open('/dev/null','w')
o,e = sys.stdout,sys.stderr
sys.stdout = sys.stderr = null
import pygame
sys.stdout = o
sys.stderr = e
null.close()
del null
# ===== END block to import pygame =====

try:
    from . import temp_file
except:
    import temp_file

def randomize_colors(sandpile_dir):
    os.chdir(sandpile_dir)
    factors = [2*random.random() for _ in range(8)]
    value_saturations = [(1 if x>1 else x, 0 if x<1 else 1-x) for x in factors]
    colors = [tuple(map(lambda x: int(x*255), colorsys.hsv_to_rgb(random.random(), b-1, a))) for a,b in value_saturations]
    hexcolors = [''.join(map(lambda x:hex(x)[2:].zfill(2), c)) for c in colors]
    with open('colors', 'w') as o:
        for line in hexcolors:
            print(line, file=o)


def sandpile_tropical_curve(width, height, sandpile_dir, coords_count=random.randint(3, 25), max_dimension=random.randint(128,192)):
    randomize_colors(sandpile_dir)
    if width>max_dimension or height>max_dimension:
        if width>height:
            scale = width/max_dimension
        else:
            scale = height/max_dimension
    else:
        scale = 1
    small_w = int(width/scale)
    small_h = int(height/scale)
    os.chdir(sandpile_dir)
    out_file = temp_file.TemporaryFile.generate_new('png')
    data = b''
    for i in range(coords_count-1):
        data += bytes(str(random.randint(0, small_w-1)), 'utf-8')+b' '+bytes(str(random.randint(0, small_h-1)), 'utf-8') + b', '
    data += bytes(str(random.randint(0, small_w-1)), 'utf-8')+b' '+bytes(str(random.randint(0, small_h-1)), 'utf-8') + b'.'
    proc = subprocess.run(['cargo','run','--release','rectangle',str(small_w)+'x'+str(small_h),'png','add','all-3','read_list',out_file],
           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
           input=data, check=True)
    image = pygame.image.load(out_file)
    image = pygame.transform.scale(image, (int(image.get_width()*scale), int(image.get_height()*scale)))
    pygame.image.save(image, out_file)
    return out_file

def sandpile_single_point(width, height, sandpile_dir, drop_width=random.randint(1,3), drop_height=random.randint(1,3), particle_count=random.randint(400, 10000), eight_way_neighborhood=False):
    randomize_colors(sandpile_dir)
    os.chdir(sandpile_dir)
    out_file = temp_file.TemporaryFile.generate_new('png')
    command = ['cargo','run','--release']
    command.append('infinite' + ('.moore' if eight_way_neighborhood else ''))
    command.append(str(drop_width)+'x'+str(drop_height))
    command.append('png')
    command.extend(['all-'+str(particle_count)])
    command.append(out_file)

    proc = subprocess.run(command,
           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
           check=True)
    
    image = pygame.image.load(out_file)
    max_dimension = max(image.get_width(), image.get_height())
    if width<height:
        scale = width/max_dimension
    else:
        scale = height/max_dimension
    image = pygame.transform.scale(image, (int(image.get_width()*scale), int(image.get_height()*scale)))
    pygame.image.save(image, out_file)
    return out_file
