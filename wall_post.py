import api
import upload

def post_one_image(path):
    api.vk.wall.post(attachments=upload.image_for_wall(path))

if __name__=='__main__':
    print('will post img to wall:')
    post_one_image(input('path: '))
