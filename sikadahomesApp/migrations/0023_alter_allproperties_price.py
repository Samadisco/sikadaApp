# Generated by Django 4.2.7 on 2024-01-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0022_alter_houselease_baths_alter_houselease_beds_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allproperties',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]