# Generated by Django 4.0.6 on 2022-09-15 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0043_alter_postcomment_commentliked_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentlike',
            name='comment_status',
        ),
    ]