# Generated by Django 3.1.3 on 2021-04-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_auto_20210327_0952"),
    ]

    operations = [
        migrations.AlterField(
            model_name="snapshot",
            name="url",
            field=models.URLField(db_index=True, unique=True),
        ),
    ]
