# Generated by Django 3.0.2 on 2020-10-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractNews', '0002_auto_20201002_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
