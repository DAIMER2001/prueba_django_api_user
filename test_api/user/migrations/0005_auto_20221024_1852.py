# Generated by Django 3.0.5 on 2022-10-24 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20221024_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='users',
            new_name='categories',
        ),
    ]