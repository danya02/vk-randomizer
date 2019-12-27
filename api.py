import vk_api
import SECRETS

if SECRETS.token:
    vk_session = vk_api.VkApi(SECRETS.login, token=SECRETS.token)
else:
    vk_session = vk_api.VkApi(SECRETS.login, SECRETS.password)
vk_session.auth()

vk = vk_session.get_api()
