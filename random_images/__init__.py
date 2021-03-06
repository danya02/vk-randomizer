import random
import colorsys
import os
from . import perlin_noise
from . import two_d_geometry
from . import two_d_plots
from . import sandpiles

width=512
height=512

topic_dict = dict()

SANDPILE_DIR = '/home/danya/sandpile'

def topics(*topic_list):
    def decorate(func):
        func.topics = topic_list
        for i in topic_list:
            fset = topic_dict.get(i, set())
            fset.add(func)
            topic_dict[i] = fset
        def decorated(*args, **kwargs):
            return func(*args, **kwargs)
        return decorated
    return decorate

@topics('noise','perlin','monochrome')
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


@topics('noise','perlin','colorful')
def colorful_perlin_noise():
    bg_color=(255,255,255)
    fg_color=(0,0,0)
    if random.random()>0.5:
        bg_color,fg_color = fg_color, bg_color

    rstep=random.random()/5
    gstep=random.random()/5
    bstep=random.random()/5
    return perlin_noise.generate_colorful(width,height,fg_color=fg_color,bg_color=bg_color,
            rpx_step=lambda x:x+rstep, rpy_step=lambda y:y+rstep,
            gpx_step=lambda x:x+gstep, gpy_step=lambda y:y+gstep,
            bpx_step=lambda x:x+bstep, bpy_step=lambda y:y+bstep, octaves=random.randint(1,7))
    
@topics('geometry','2d','lines','monochrome')
def mono_lines():
    return two_d_geometry.straight_lines_mono(width, height)

@topics('geometry','2d','lines','colorful')
def color_lines():
    return two_d_geometry.straight_lines_color(width, height)

@topics('geometry','2d','polygons','triangles','colorful')
def color_tris():
    return two_d_geometry.triangles(width,height)

# commented out because it doesn't look all that nice.
#@topics('geometry','2d','polygons','triangles','monochrome')
#def mono_tris():
#    n = random.random()
#    return two_d_geometry.triangles(width,height, bg_color=(0,0,0), fg_color_fn=lambda: (int(i*255) for i in colorsys.hsv_to_rgb(n,1,1)))

@topics('geometry','2d','circles','continuous','arcs','colorful')
def color_tris():
    return two_d_geometry.circles(width,height)

@topics('math','2d','plot','polynominal')
def polynom():
    return two_d_plots.plot_random_polynominal()

@topics('math','2d','sandpile','tropical_curve')
def tropical_curve():
    if not os.path.exists(SANDPILE_DIR):
        print('Tried to run a sandpile, but the dir for sandpiles did not exist')
        return get_any()
    return sandpiles.sandpile_tropical_curve(width, height, SANDPILE_DIR)

@topics('math','2d','sandpile','sandpile_infinite', 'von-neumann')
def single_point_sandpile():
    if not os.path.exists(SANDPILE_DIR):
        print('Tried to run a sandpile, but the dir for sandpiles did not exist')
        return get_any()
    return sandpiles.sandpile_single_point(width, height, SANDPILE_DIR)

@topics('math','2d','sandpile','sandpile_infinite', 'moore')
def single_point_sandpile_moore():
    if not os.path.exists(SANDPILE_DIR):
        print('Tried to run a sandpile, but the dir for sandpiles did not exist')
        return get_any()
    return sandpiles.sandpile_single_point(width, height, SANDPILE_DIR, eight_way_neighborhood=True)

def get_by_topic(*topic_list):
    opts = topic_dict[topic_list[0]]
    for i in topic_list[1:]:
        opts = opts.intersection(topic_dict[i])
    return random.choice(list(opts))()

def get_any():
#    return get_by_topic('moore')
    actions = set()
    for i in topic_dict:
        actions.update(topic_dict[i])
    return random.choice(list(actions))()
