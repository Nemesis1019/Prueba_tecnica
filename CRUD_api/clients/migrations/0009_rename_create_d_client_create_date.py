# Generated by Django 4.2.2 on 2023-06-07 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_alter_client_create_d'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='create_d',
            new_name='create_date',
        ),
    ]
