# Generated by Django 4.2.7 on 2023-12-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0009_landsale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landsale',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
        migrations.AlterField(
            model_name='landsale',
            name='video',
            field=models.ImageField(blank=True, null=True, upload_to='houseRent'),
        ),
    ]