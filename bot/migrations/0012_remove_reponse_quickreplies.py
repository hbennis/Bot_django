# Generated by Django 2.0.2 on 2018-03-23 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_reponse_quickreplies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reponse',
            name='quickreplies',
        ),
    ]
