# Generated by Django 3.0.5 on 2022-10-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20221024_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='users',
            field=models.ManyToManyField(related_name='categories', to='user.Category'),
        ),
    ]