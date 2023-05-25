# Generated by Django 4.2.1 on 2023-05-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, null=True, unique=True)),
                ("description", models.TextField(null=True)),
                ("duration", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "movies",
            },
        ),
    ]