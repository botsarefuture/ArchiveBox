# Generated by Django 3.1.3 on 2021-02-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_auto_20210218_0729"),
    ]

    operations = [
        migrations.AlterField(
            model_name="snapshot",
            name="title",
            field=models.CharField(
                blank=True, db_index=True, max_length=1024, null=True
            ),
        ),
    ]
