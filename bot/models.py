from django.db import models
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# @python_2_unicode_compatible
# class Reponse(models.Model):
#     reponse = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     source = models.TextField(blank = True, null = True, default='None')
#     name = models.TextField(blank = True, null = True, default='None')
#     success = models.NullBooleanField(blank=True, default=True)
#     error = models.TextField(blank=True, null=True, default='None')
#
#     def __str__(self):
#         return self.reponse
#
#     @permalink
#     def get_absolute_url(self):
#         return ('view_blog_category', None, {'reponse': self.reponse})


class Tokens(models.Model):
    subject =models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)


class Users_bdd(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    connected = models.BooleanField(blank=True, default=True)
    current_subject = models.CharField(max_length=100)
    #subjects_done = models.ForeignKey(Discussion, on_delete=models.CASCADE)

# class Subjects(models.Model):
#     subject = models.CharField(max_length=100)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     value = models.BooleanField(blank=True, default=False)
#     subject = models.CharField(max_length=100)
#     token = models.CharField(max_length=100)
#     difficulty = models.CharField(max_length=100)
#
#
class Discussion(models.Model):
    subject = models.CharField(max_length=100)
    reponse = models.CharField(max_length=100)
    uid = models.ForeignKey(Users_bdd, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.TextField(blank=True, null=True, default='None')
    success = models.NullBooleanField(blank=True, default=True)
    error = models.TextField(blank=True, null=True, default='None')