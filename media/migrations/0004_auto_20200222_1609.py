# Generated by Django 3.0.1 on 2020-02-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20200208_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
