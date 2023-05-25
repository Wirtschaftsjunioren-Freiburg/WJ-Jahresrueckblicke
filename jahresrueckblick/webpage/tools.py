import os
from PIL import Image
from django.conf import settings

def cropImage(original):
    # check if cropped file exists
    if original.url.replace(settings.MEDIA_URL, settings.MEDIA_ROOT+'cropped/') in os.listdir(settings.MEDIA_ROOT+'cropped/'):
        return original.url.replace(settings.MEDIA_URL, settings.MEDIA_URL+'cropped/')
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
        image.thumbnail((1200, 1200), Image.ANTIALIAS)
        image.save(settings.MEDIA_ROOT+'cropped/' + original.url.replace(settings.MEDIA_URL, '').replace(['ä', 'ö', 'ü', 'ß'], ['ae', 'oe', 'ue', 'ss']))
        return original.url.replace(settings.MEDIA_URL, settings.MEDIA_URL+'cropped/').replace(['ä', 'ö', 'ü', 'ß'], ['ae', 'oe', 'ue', 'ss'])