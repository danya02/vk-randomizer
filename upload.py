import api
import vk_api.upload

def set_profile_photo(path):
    uploader = vk_api.upload.VkUpload(api.vk)
    uploader.photo_profile(path)

def image_for_wall(path, caption=None):
    uploader = vk_api.upload.VkUpload(api.vk)
    obj = uploader.photo_wall(path, caption=caption)[0]
    return 'photo'+str(obj['owner_id'])+'_'+str(obj['id'])
