# Generated by Django 4.1 on 2022-08-31 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_alter_post_postuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileupload',
            name='cover_img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='cover_image'),
        ),
        migrations.AddField(
            model_name='profileupload',
            name='detail',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profileupload',
            name='hobbies',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profileupload',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profileupload',
            name='img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_image'),
        ),
    ]