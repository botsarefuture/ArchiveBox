# Generated by Django 3.0.8 on 2020-10-12 15:20

from django.db import migrations, models
from django.utils.text import slugify


def forwards_func(apps, schema_editor):
    SnapshotModel = apps.get_model("core", "Snapshot")
    TagModel = apps.get_model("core", "Tag")

    db_alias = schema_editor.connection.alias
    snapshots = SnapshotModel.objects.all()
    for snapshot in snapshots:
        tags = snapshot.tags
        tag_set = set(tag.strip() for tag in (snapshot.tags_old or "").split(","))
        tag_set.discard("")

        for tag in tag_set:
            to_add, _ = TagModel.objects.get_or_create(
                name=tag, defaults={"slug": slugify(tag)}
            )
            snapshot.tags.add(to_add)


def reverse_func(apps, schema_editor):
    SnapshotModel = apps.get_model("core", "Snapshot")
    TagModel = apps.get_model("core", "Tag")

    db_alias = schema_editor.connection.alias
    snapshots = SnapshotModel.objects.all()
    for snapshot in snapshots:
        tags = snapshot.tags.values_list("name", flat=True)
        snapshot.tags_old = ",".join([tag for tag in tags])
        snapshot.save()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_auto_20200728_0326"),
    ]

    operations = [
        migrations.RenameField(
            model_name="snapshot",
            old_name="tags",
            new_name="tags_old",
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="name"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=100, unique=True, verbose_name="slug"),
                ),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.AddField(
            model_name="snapshot",
            name="tags",
            field=models.ManyToManyField(to="core.Tag"),
        ),
        migrations.RunPython(forwards_func, reverse_func),
        migrations.RemoveField(
            model_name="snapshot",
            name="tags_old",
        ),
    ]
