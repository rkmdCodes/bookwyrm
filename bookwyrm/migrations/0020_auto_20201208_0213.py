# Generated by Django 3.0.7 on 2020-12-08 02:13

import bookwyrm.models.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0019_auto_20201130_1939"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="aliases",
            field=bookwyrm.models.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="bio",
            field=bookwyrm.models.fields.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="author",
            name="born",
            field=bookwyrm.models.fields.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="author",
            name="died",
            field=bookwyrm.models.fields.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=bookwyrm.models.fields.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="author",
            name="openlibrary_key",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="wikipedia_link",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="authors",
            field=bookwyrm.models.fields.ManyToManyField(to="bookwyrm.Author"),
        ),
        migrations.AlterField(
            model_name="book",
            name="cover",
            field=bookwyrm.models.fields.ImageField(
                blank=True, null=True, upload_to="covers/"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="description",
            field=bookwyrm.models.fields.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="first_published_date",
            field=bookwyrm.models.fields.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="goodreads_key",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="languages",
            field=bookwyrm.models.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="librarything_key",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="openlibrary_key",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="published_date",
            field=bookwyrm.models.fields.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="series",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="series_number",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="sort_title",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="subject_places",
            field=bookwyrm.models.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="subjects",
            field=bookwyrm.models.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="subtitle",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=bookwyrm.models.fields.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="boost",
            name="boosted_status",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="boosters",
                to="bookwyrm.Status",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="book",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="bookwyrm.Edition"
            ),
        ),
        migrations.AlterField(
            model_name="edition",
            name="asin",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="edition",
            name="isbn_10",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="edition",
            name="isbn_13",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="edition",
            name="oclc_number",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="edition",
            name="pages",
            field=bookwyrm.models.fields.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="edition",
            name="parent_work",
            field=bookwyrm.models.fields.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="editions",
                to="bookwyrm.Work",
            ),
        ),
        migrations.AlterField(
            model_name="edition",
            name="physical_format",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="edition",
            name="publishers",
            field=bookwyrm.models.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="favorite",
            name="status",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="bookwyrm.Status"
            ),
        ),
        migrations.AlterField(
            model_name="favorite",
            name="user",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="caption",
            field=bookwyrm.models.fields.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=bookwyrm.models.fields.ImageField(
                blank=True, null=True, upload_to="status/"
            ),
        ),
        migrations.AlterField(
            model_name="quotation",
            name="book",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="bookwyrm.Edition"
            ),
        ),
        migrations.AlterField(
            model_name="quotation",
            name="quote",
            field=bookwyrm.models.fields.TextField(),
        ),
        migrations.AlterField(
            model_name="review",
            name="book",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="bookwyrm.Edition"
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="name",
            field=bookwyrm.models.fields.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=bookwyrm.models.fields.IntegerField(
                blank=True,
                default=None,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="shelf",
            name="name",
            field=bookwyrm.models.fields.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="shelf",
            name="privacy",
            field=bookwyrm.models.fields.CharField(
                choices=[
                    ("public", "Public"),
                    ("unlisted", "Unlisted"),
                    ("followers", "Followers"),
                    ("direct", "Direct"),
                ],
                default="public",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="shelf",
            name="user",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="shelfbook",
            name="added_by",
            field=bookwyrm.models.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="shelfbook",
            name="book",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="bookwyrm.Edition"
            ),
        ),
        migrations.AlterField(
            model_name="shelfbook",
            name="shelf",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="bookwyrm.Shelf"
            ),
        ),
        migrations.AlterField(
            model_name="status",
            name="content",
            field=bookwyrm.models.fields.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="status",
            name="mention_books",
            field=bookwyrm.models.fields.TagField(
                related_name="mention_book", to="bookwyrm.Edition"
            ),
        ),
        migrations.AlterField(
            model_name="status",
            name="mention_users",
            field=bookwyrm.models.fields.TagField(
                related_name="mention_user", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="status",
            name="published_date",
            field=bookwyrm.models.fields.DateTimeField(
                default=django.utils.timezone.now
            ),
        ),
        migrations.AlterField(
            model_name="status",
            name="reply_parent",
            field=bookwyrm.models.fields.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="bookwyrm.Status",
            ),
        ),
        migrations.AlterField(
            model_name="status",
            name="sensitive",
            field=bookwyrm.models.fields.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="status",
            name="user",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=bookwyrm.models.fields.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="userblocks",
            name="user_object",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="userblocks_user_object",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userblocks",
            name="user_subject",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="userblocks_user_subject",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollowrequest",
            name="user_object",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="userfollowrequest_user_object",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollowrequest",
            name="user_subject",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="userfollowrequest_user_subject",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollows",
            name="user_object",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="userfollows_user_object",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollows",
            name="user_subject",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="userfollows_user_subject",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="usertag",
            name="book",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="bookwyrm.Edition"
            ),
        ),
        migrations.AlterField(
            model_name="usertag",
            name="tag",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="bookwyrm.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="usertag",
            name="user",
            field=bookwyrm.models.fields.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="work",
            name="default_edition",
            field=bookwyrm.models.fields.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="bookwyrm.Edition",
            ),
        ),
        migrations.AlterField(
            model_name="work",
            name="lccn",
            field=bookwyrm.models.fields.CharField(
                blank=True, max_length=255, null=True
            ),
        ),
    ]
