# Generated by Django 4.2.5 on 2023-09-26 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'заявка', 'verbose_name_plural': 'заявки'},
        ),
    ]
