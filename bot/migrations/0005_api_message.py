# Generated by Django 2.0.2 on 2018-03-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_reponse_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='API_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField(blank=True, default='None', null=True)),
            ],
        ),
    ]
