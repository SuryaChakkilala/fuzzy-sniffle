# Generated by Django 4.1 on 2023-05-04 17:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="AppImage",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="BusinessSystem",
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
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("number", models.IntegerField()),
                ("instructions", models.TextField()),
                ("questions", models.TextField()),
                ("score_required", models.BooleanField(default=True)),
                ("time_of_attendance", models.TimeField(null=True)),
                ("time_of_review", models.TimeField()),
                ("date_of_review", models.DateField()),
                ("attendance_open", models.BooleanField(default=True)),
                ("scoring_open", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("number", models.CharField(max_length=10, unique=True)),
                (
                    "floor",
                    models.CharField(
                        choices=[
                            ("Ground Floor", "Ground Floor"),
                            ("First Floor", "First Floor"),
                            ("Second Floor", "Second Floor"),
                            ("Third Floor", "Third Floor"),
                            ("Fourth Floor", "Fourth Floor"),
                            ("Fifth Floor", "Fifth Floor"),
                            ("Sixth Floor", "Sixth Floor"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("registration_no", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=1024)),
                ("cluster", models.IntegerField(blank=True, default=1)),
                ("course", models.CharField(max_length=4)),
                ("number", models.IntegerField()),
                (
                    "business_system",
                    models.ForeignKey(
                        db_column="bs_name",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pages.businesssystem",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeamReviewRoom",
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
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.review"
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pages.room",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.team"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentReviewScore",
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
                ("comments", models.TextField(max_length=2000)),
                ("score", models.IntegerField(default=0)),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.review"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.student"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentReviewAttendance",
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
                ("absent", models.BooleanField(default=False)),
                (
                    "posted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.review"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.student"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="student",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pages.team"
            ),
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("registration_no", models.CharField(max_length=10)),
                (
                    "issue_type",
                    models.CharField(
                        choices=[
                            ("Faculty Absent", "Faculty Absent"),
                            ("Web Application Issue", "Web Application Issue"),
                            ("WIFI issue", "Network Connectivity"),
                            ("Others", "Others"),
                        ],
                        max_length=500,
                    ),
                ),
                ("issue", models.TextField(max_length=10000)),
                ("complaint_raised_time", models.DateTimeField(auto_now_add=True)),
                ("resolved", models.BooleanField(default=False)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.room"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Announcement",
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
                ("title", models.CharField(max_length=300)),
                ("content", models.CharField(max_length=1025)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Room Change", "Room Change"),
                            ("Disciplinary Activities", "Disciplinary Activities"),
                            ("Facilities", "Facilities"),
                            ("Others", "Others"),
                        ],
                        max_length=1000,
                        null=True,
                    ),
                ),
                ("recorded_date", models.DateField(auto_now_add=True)),
                ("recorded_time", models.TimeField(auto_now_add=True)),
                ("important", models.BooleanField(default=False)),
                ("groups", models.ManyToManyField(to="auth.group")),
            ],
        ),
        migrations.CreateModel(
            name="TeamProgress",
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
                ("description", models.TextField()),
                (
                    "self_rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                ("submission_time", models.DateTimeField(auto_now_add=True)),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.review"
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.team"
                    ),
                ),
            ],
            options={"managed": True, "unique_together": {("team", "review")},},
        ),
    ]
