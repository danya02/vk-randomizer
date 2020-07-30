from . import download
from . import img_filter
from . import post


def post_images(api, count):
    images = download.get_any(count)
    filtered_images = list(map(img_filter.apply_filters, images))
    poster = post.StoriesUploader(api)
    uploads = list(map(poster.upload_photo, filtered_images))
    return uploads
