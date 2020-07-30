import upload
import wall_post
import random_images
import random
import stories
import api

def update_profile_picture():
    picture = random_images.get_any()
    upload.set_profile_photo(picture)

def post_wall_picture():
    picture = random_images.get_any()
    wall_post.post_one_image(picture)

def post_story():
    stories.post_images(api.vk, random.randint(1, 3))

def do_anything():
    actions = [update_profile_picture, post_wall_picture, post_story]
    this_action = random.choice(actions)
    this_action()

if __name__=='__main__':
    do_anything()
