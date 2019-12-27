import api
import vk_api.upload

def set_profile_photo(path):
    uploader = vk_api.upload.VkUpload(api.vk)
    uploader.photo_profile(path)

if __name__=='__main__':
    print('Will upload photo as profile image:')
    set_profile_photo(input('path: '))
