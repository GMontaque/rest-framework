# Generated by Django 3.2.25 on 2024-07-10 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_q35ywj', upload_to='images/'),
        ),
    ]
