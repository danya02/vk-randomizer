import vk_api
import requests


class StoriesUploader:
    def __init__(self, api):
        self.api = api
        self.upload_results = []

    def save(self):
        return self.api.stories.save(upload_results=','.join(self.upload_result))

    def upload_photo(self, photo):
        upload_url = self.api.stories.getPhotoUploadServer(add_to_news=1)['upload_url']
        result = requests.post(upload_url, files={'file': open(str(photo), 'rb')}).json()
        return result
