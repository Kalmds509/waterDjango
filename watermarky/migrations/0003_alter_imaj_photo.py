# Generated by Django 4.1 on 2022-09-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watermarky', '0002_imaj_delete_imajes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imaj',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
