# Generated by Django 2.0.2 on 2018-03-23 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_auto_20180323_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reponse',
            old_name='username',
            new_name='name',
        ),
    ]