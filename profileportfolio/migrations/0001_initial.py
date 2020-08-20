# Generated by Django 3.0.6 on 2020-08-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image/images/')),
                ('url_link', models.URLField(blank=True)),
            ],
        ),
    ]
