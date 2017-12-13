from django.db import models
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Reponse(models.Model):
    reponse = models.CharField(max_length=100)

    def __str__(self):
        return self.reponse

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'reponse': self.reponse})

