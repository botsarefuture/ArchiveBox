# Generated by Django 3.1.3 on 2021-03-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_auto_20210219_0211"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
