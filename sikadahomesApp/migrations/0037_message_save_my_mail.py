# Generated by Django 5.0.1 on 2024-03-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikadahomesApp', '0036_message_phone_message_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='save_my_mail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]