# Generated by Django 4.1.3 on 2022-12-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_alter_submission_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="enrollment",
            name="is_ended",
            field=models.BooleanField(default=False),
        ),
    ]