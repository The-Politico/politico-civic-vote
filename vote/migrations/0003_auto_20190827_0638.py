# Generated by Django 2.2.4 on 2019-08-27 06:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("geography", "0002_point_pointlabeloffset"),
        ("vote", "0002_votes_runoff"),
    ]

    operations = [
        migrations.AddField(
            model_name="delegates",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 1, 1, 0, 0, tzinfo=utc),
                editable=False,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="delegates",
            name="uid",
            field=models.CharField(blank=True, editable=False, max_length=500),
        ),
        migrations.AddField(
            model_name="delegates",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 1, 1, 0, 0, tzinfo=utc),
                editable=False,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="electoralvotes",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 1, 1, 0, 0, tzinfo=utc),
                editable=False,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="electoralvotes",
            name="uid",
            field=models.CharField(blank=True, editable=False, max_length=500),
        ),
        migrations.AddField(
            model_name="electoralvotes",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 1, 1, 0, 0, tzinfo=utc),
                editable=False,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="votes",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 1, 1, 0, 0, tzinfo=utc),
                editable=False,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="votes",
            name="uid",
            field=models.CharField(blank=True, editable=False, max_length=500),
        ),
        migrations.AddField(
            model_name="votes",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 1, 1, 0, 0, tzinfo=utc),
                editable=False,
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="delegates",
            unique_together={("candidate_election", "division")},
        ),
        migrations.AlterUniqueTogether(
            name="electoralvotes",
            unique_together={("candidate_election", "division")},
        ),
        migrations.AlterUniqueTogether(
            name="votes",
            unique_together={
                ("ballot_answer", "candidate_election", "division")
            },
        ),
    ]
