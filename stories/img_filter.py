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
import os
import random
from . import temp_file
import cairosvg
from . import allowable_images

current_path = os.path.dirname(os.path.abspath(__file__))

filters = []

def filter(func):
    filters.append(func)
    return func

@filter
def add_emoji(image):
    data_dir = os.path.join(current_path, 'twemoji-color-font', 'assets', 'twemoji-svg')
    options = set(os.listdir(data_dir))
    options = list(options.intersection(allowable_images.get_allowable_images()))
    used_img = random.choice(options)
    used_img = os.path.join(data_dir, used_img)

    save_to = temp_file.TemporaryFile.generate_new('png')
    cairosvg.svg2png(url=used_img, write_to=str(save_to), scale=10)
    emoji = pygame.image.load(str(save_to))

    emoji = pygame.transform.rotate(emoji, (random.random() - 0.5) * 180 ) # rotate up to 90 degrees to either direction
    cw,ch = emoji.get_size()
    fac = random.random()/2 + 0.5 # from 0.5 to 1
    emoji = pygame.transform.scale(emoji, (int(cw*fac), int(ch*fac)) )

    emoji_rect = emoji.get_rect()
    target_rect = image.get_rect()
    emoji_rect.centerx = random.randint(0, image.get_width())
    emoji_rect.centery = random.randint(0, image.get_height())
    emoji_rect.clamp_ip(target_rect)

    image.blit(emoji, emoji_rect)
    return image

def apply_filters(image_path, count=random.randint(3, 9)):
    image = pygame.image.load(str(image_path))
    for _ in range(count):
        image = random.choice(filters)(image)
    pygame.image.save(image, str(image_path))
    return image_path
