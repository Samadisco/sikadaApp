# Generated by Django 5.0.1 on 2024-05-01 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0038_rename_propety_ids_cart_propety_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='propety_id',
            new_name='property_id',
        ),
    ]
