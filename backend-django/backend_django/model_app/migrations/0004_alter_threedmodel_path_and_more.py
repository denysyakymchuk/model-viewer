# Generated by Django 5.0.6 on 2024-06-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0003_alter_threedmodel_path_env_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threedmodel',
            name='path',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='threedmodel',
            name='path_env_image',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='threedmodel',
            name='path_skybox_image',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
