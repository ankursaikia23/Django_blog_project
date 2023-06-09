# Generated by Django 4.2 on 2023-05-10 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_remove_comment_create_date_comment_created_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 4, 51, 18, 51890, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 4, 51, 18, 51890, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
