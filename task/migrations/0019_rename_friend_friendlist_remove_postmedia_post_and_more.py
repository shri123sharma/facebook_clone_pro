# Generated by Django 4.1 on 2022-09-01 18:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0018_alter_profileupload_profileuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friend',
            new_name='FriendList',
        ),
        migrations.RemoveField(
            model_name='postmedia',
            name='post',
        ),
        migrations.DeleteModel(
            name='MessagePost',
        ),
        migrations.DeleteModel(
            name='PostMedia',
        ),
    ]
