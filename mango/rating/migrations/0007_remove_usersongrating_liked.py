# Generated by Django 5.0.6 on 2024-07-17 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0006_remove_usersongrating_song_usersongrating_album_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersongrating',
            name='liked',
        ),
    ]
