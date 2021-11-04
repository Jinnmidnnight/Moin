# Generated by Django 3.2.2 on 2021-11-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0004_remove_open_1_like_users'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='openapp.Open_1'),
        ),
    ]
