# Generated by Django 4.1.2 on 2022-12-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
