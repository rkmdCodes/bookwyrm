# Generated by Django 3.1.6 on 2021-04-08 15:56

import bookwyrm.models.fields
import django.contrib.postgres.fields.citext
import django.contrib.postgres.operations
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0062_auto_20210407_1545"),
    ]

    operations = [
        django.contrib.postgres.operations.CITextExtension(),
        migrations.AlterField(
            model_name="user",
            name="localname",
            field=django.contrib.postgres.fields.citext.CICharField(
                max_length=255,
                null=True,
                unique=True,
                validators=[bookwyrm.models.fields.validate_localname],
            ),
        ),
    ]
