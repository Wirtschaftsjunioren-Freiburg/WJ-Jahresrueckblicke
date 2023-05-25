import os
from PIL import Image
from django.conf import settings

def cropImage(original):
    translation_table = str.maketrans({'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss', '%': ''})
    # check if cropped file exists
    croppedPath = original.url.replace(settings.MEDIA_URL, settings.MEDIA_ROOT+'cropped/').lower().translate(translation_table)
    croppedUrl = original.url.replace(settings.MEDIA_URL, settings.MEDIA_URL+'cropped/').lower().translate(translation_table)
    if os.path.isfile(croppedPath):
        return croppedUrl
    else:
        # crop image
        try:
            image = Image.open(original)
        except:
            return original.url
        # crop image to aspect ration 16:9 and max width and height 1200px
        width, height = image.size
        if width/height > 16/9:
            image = image.crop(((width-height*16/9)/2, 0, width-(width-height*16/9)/2, height))
        else:
            image = image.crop((0, (height-width*9/16)/2, width, height-(height-width*9/16)/2))
        image.thumbnail((500, 500), Image.ANTIALIAS)
        image.save(croppedPath, quality=80)
        return croppedUrl