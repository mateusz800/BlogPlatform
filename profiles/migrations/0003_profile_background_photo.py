# Generated by Django 3.0.1 on 2020-02-25 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_auto_20200222_1609'),
        ('profiles', '0002_auto_20200222_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='background_photo', to='media.Photo'),
        ),
    ]
