# Generated by Django 4.2.5 on 2023-09-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_alter_house_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='houses/photos', verbose_name='фотография'),
        ),
    ]