# Generated by Django 4.2 on 2023-05-10 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_comment_created_date_alter_post_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 15, 42, 37, 931139, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
