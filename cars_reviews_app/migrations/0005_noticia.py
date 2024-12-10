# Generated by Django 5.1.3 on 2024-11-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_reviews_app', '0004_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
