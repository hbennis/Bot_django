# Generated by Django 2.0.2 on 2018-03-23 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_auto_20180314_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reponse',
            old_name='name',
            new_name='username',
        ),
    ]