from django.db import models
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Reponse(models.Model):
    reponse = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.TextField(blank = True, null = True, default='None')
    name = models.TextField(blank = True, null = True, default='None')
    success = models.NullBooleanField(blank=True, default=True)
    error = models.TextField(blank=True, null=True, default='None')
    quickreplies = models.TextField(blank=True, null=True, default='None')

    def __str__(self):
        return self.reponse

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'reponse': self.reponse})



