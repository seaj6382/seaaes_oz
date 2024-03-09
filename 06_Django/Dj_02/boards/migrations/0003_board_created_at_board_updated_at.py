# Generated by Django 5.0.3 on 2024-03-08 06:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("boards", "0002_board_date_board_likes_board_reviews_board_writer"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="board",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
