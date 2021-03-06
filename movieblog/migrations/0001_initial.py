# Generated by Django 3.0.5 on 2021-01-20 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=50, verbose_name='Movie Title')),
                ('movie_description', models.TextField(blank=True, default=None, null=True, verbose_name='Movie Description')),
                ('movie_date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('movie_images', models.ImageField(blank=True, default=None, null=True, upload_to='posters', verbose_name='Upload Poster')),
                ('movie_imdb_plugin', models.TextField(blank=True, default=None, null=True, verbose_name='IMDB Plugin')),
                ('movie_video_length', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Movie Duration')),
                ('movie_director', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Movie Director')),
                ('movie_actors', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Movie Actors')),
                ('movie_genres', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Movie Genres')),
                ('movie_trailer', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Movie Trailer')),
                ('movie_streaming_partner', models.CharField(blank=True, choices=[('netflix', 'Netflix'), ('primevideo', 'Primevideo'), ('hotstar', 'Disney+ Hotstar'), ('sonyliv', 'SonyLiv'), ('zee5', 'Zee5'), ('youtube', 'YouTube'), ('hbomax', 'HBO Max'), ('altbalaji', 'ALT Balaji')], default=None, max_length=1000, null=True, verbose_name='Movie Stream')),
                ('movie_streaming_link', models.TextField(blank=True, default=None, null=True, verbose_name='Streaming Link')),
                ('movie_audio', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Audio')),
                ('movie_available_youtube', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Available on Youtube')),
            ],
        ),
    ]
