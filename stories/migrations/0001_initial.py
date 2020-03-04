# Generated by Django 3.0.1 on 2020-02-21 18:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('media', '0003_auto_20200208_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(unique_for_date='published_date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='profiles.Profile')),
                ('featured_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article_cover', to='media.Photo')),
            ],
            options={
                'ordering': ('-published_date',),
            },
        ),
    ]
