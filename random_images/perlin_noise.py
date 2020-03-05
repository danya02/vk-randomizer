import noise
import pygame
from . import temp_file
import random


def clamp(a):
    return min(255,max(0,abs(int(a))))

def clamp_fac(a):
    return min(1,max(0,a))

def generate_monochrome(width, height,zoff=0,
        fg_color=(255,255,255), bg_color=(0,0,0),
        px=random.randint(-100000,100000)+random.random(),
        py=random.randint(-100000,100000)+random.random(),
        octaves=4, fac_boost=lambda x:x*4,
        px_step=lambda x:x+0.005, py_step=lambda y:y+0.005):
    surface = pygame.Surface((width, height))
    surface.fill(pygame.Color(*bg_color))
    px_init = px
    buf = pygame.PixelArray(surface)
    for y in range(height):
        px = px_init
        for x in range(width):
            t = clamp_fac(fac_boost(noise.pnoise3(px,py,zoff, octaves=octaves)))
            buf[x,y] = (
                    clamp(bg_color[0] + t * (fg_color[0] - bg_color[0])),
                    clamp(bg_color[1] + t * (fg_color[1] - bg_color[1])),
                    clamp(bg_color[2] + t * (fg_color[2] - bg_color[2]))
                    )
            px = px_step(px)
        py = py_step(py)
    del buf
    tf = temp_file.TemporaryFile.generate_new('png')
    pygame.image.save(surface, tf)
    return tf

def generate_colorful(width, height, zoff=0,
        bg_color=(0,0,0), fg_color=(255,255,255),
        rpx=random.randint(-100000,100000)+random.random(),
        rpy=random.randint(-100000,100000)+random.random(),
        gpx=random.randint(-100000,100000)+random.random(),
        gpy=random.randint(-100000,100000)+random.random(),
        bpx=random.randint(-100000,100000)+random.random(),
        bpy=random.randint(-100000,100000)+random.random(),
        octaves=4, fac_boost=lambda x:x*2,
        rpx_step=lambda x:x+0.005, rpy_step=lambda y:y+0.005,
        gpx_step=lambda x:x+0.005, gpy_step=lambda y:y+0.005,
        bpx_step=lambda x:x+0.005, bpy_step=lambda y:y+0.005):
    surface = pygame.Surface((width, height))
    surface.fill(pygame.Color(*bg_color))
    rpx_init = rpx
    gpx_init = gpx
    bpx_init = bpx
    buf = pygame.PixelArray(surface)
    for y in range(height):
        rpx = rpx_init
        gpx = gpx_init
        bpx = bpx_init
        for x in range(width):
            rt = clamp_fac(fac_boost(noise.pnoise3(rpx,rpy,zoff, octaves=octaves)))
            gt = clamp_fac(fac_boost(noise.pnoise3(gpx,gpy,zoff, octaves=octaves)))
            bt = clamp_fac(fac_boost(noise.pnoise3(bpx,bpy,zoff, octaves=octaves)))
            buf[x,y] = (
                    clamp(bg_color[0] + rt * (fg_color[0] - bg_color[0])),
                    clamp(bg_color[1] + gt * (fg_color[1] - bg_color[1])),
                    clamp(bg_color[2] + bt * (fg_color[2] - bg_color[2]))
                    )
            rpx = rpx_step(rpx)
            gpx = gpx_step(gpx)
            bpx = bpx_step(bpx)
        rpy = rpy_step(rpy)
        gpy = gpy_step(gpy)
        bpy = bpy_step(bpy)
    del buf
    tf = temp_file.TemporaryFile.generate_new('png')
    pygame.image.save(surface, tf)
    return tf
    
if __name__=='__main__':
    print(generate_colorful(1024,1024, fg_color=(0,0,0), bg_color=(255,255,255)).persist())

