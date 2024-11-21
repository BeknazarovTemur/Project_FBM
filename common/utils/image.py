import os

from PIL import Image


def image_compressor(instance):
    with Image.open(instance.file) as photo:
        aspect_ratio = photo.size[0] / photo.size[1]
        new_height = 512 / aspect_ratio
        photo.thumbnail((512, new_height))

        thumb_path = f'media/thumbnails/{os.path.basename(instance.file.name)}'
        photo.save(thumb_path, photo.format)

        instance.thumbnail = thumb_path
