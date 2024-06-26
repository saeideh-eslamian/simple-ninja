# Generated by Django 5.0.6 on 2024-06-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud_ninja", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="student_image/"),
        ),
        migrations.AddField(
            model_name="teacher",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="teacher_image/"),
        ),
    ]
