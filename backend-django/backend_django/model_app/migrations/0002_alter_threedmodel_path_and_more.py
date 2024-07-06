# Generated by Django 5.0.6 on 2024-06-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threedmodel',
            name='path',
            field=models.FileField(upload_to='3d_models/'),
        ),
        migrations.AlterField(
            model_name='threedmodel',
            name='path_env_image',
            field=models.FileField(upload_to='env_images/'),
        ),
        migrations.AlterField(
            model_name='threedmodel',
            name='path_skybox_image',
            field=models.FileField(upload_to='skybox_images/'),
        ),
    ]
