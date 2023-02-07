# Generated by Django 4.1 on 2023-02-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0009_friend_delete_friendship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]