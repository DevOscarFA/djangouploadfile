from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from datetime import datetime

import os, time
from uuid import uuid4


def upload_pdf_validator(upload_obj):
    #[0] = returns path+filename
    ext = os.path.splitext(upload_obj.name)[1]  
    valid_extension = ['.jpg','.png']
    if not ext in valid_extension:
        raise ValidationError(u'Unsupported file extension, .jpg and .png only.')

@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        f_name = '-'.join(filename.replace('.'+ext, '').split() )
        rand_strings = ''
        filename = '{}-{}{}.{}'.format(f_name, rand_strings, uuid4().hex, ext)
        return os.path.join(self.path, filename)
    

class Attach(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    image = models.FileField(upload_to=PathAndRename("images/uploads/{}".format(time.strftime("%Y/%m/%d"))),
                            validators=[upload_pdf_validator])
    image.short_description = 'Image'
    publish_date = models.DateTimeField(default=datetime.now())
    active = models.BooleanField(default=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" />' % os.path.join(settings.MEDIA_URL, str(self.image)))
    
    def __str__(self):
        return '{}'.format(self.title)
    