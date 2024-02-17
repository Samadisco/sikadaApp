# Generated by Django 4.2.7 on 2024-01-23 21:00

from django.db import migrations, models
import sikadahomesApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0021_alter_houserent_img_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houselease',
            name='baths',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houselease',
            name='beds',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houselease',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houselease',
            name='img_front',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseLease.image_upload_path),
        ),
        migrations.AlterField(
            model_name='houselease',
            name='img_gallery_1',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseLease.image_upload_path),
        ),
        migrations.AlterField(
            model_name='houselease',
            name='img_gallery_2',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseLease.image_upload_path),
        ),
        migrations.AlterField(
            model_name='houselease',
            name='img_gallery_3',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseLease.image_upload_path),
        ),
        migrations.AlterField(
            model_name='houselease',
            name='img_listing',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseLease.image_upload_path),
        ),
        migrations.AlterField(
            model_name='houselease',
            name='rooms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houselease',
            name='year_built',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='baths',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='beds',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='img_listing',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseRent.image_upload_path),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='rooms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='houserent',
            name='year_built',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='baths',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='beds',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='img_front',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseSale.image_upload_path),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='img_gallery_1',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseSale.image_upload_path),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='img_gallery_2',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseSale.image_upload_path),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='img_gallery_3',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseSale.image_upload_path),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='img_listing',
            field=models.ImageField(blank=True, null=True, upload_to=sikadahomesApp.models.HouseSale.image_upload_path),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='rooms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='housesale',
            name='year_built',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
