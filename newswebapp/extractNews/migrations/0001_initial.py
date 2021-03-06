# Generated by Django 3.0.2 on 2020-10-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceId', models.CharField(max_length=50)),
                ('sourceName', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=200)),
                ('urlToImage', models.CharField(max_length=200)),
                ('publishedAt', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
    ]
