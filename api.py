import vk_api
import SECRETS

if SECRETS.token:
    vk_session = vk_api.VkApi(SECRETS.login, token=SECRETS.token, app_id=6489309)
else:
    vk_session = vk_api.VkApi(SECRETS.login, SECRETS.password, app_id=6489309)
    vk_session.auth()

vk = vk_session.get_api()
