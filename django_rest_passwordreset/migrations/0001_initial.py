# Generated by Django 4.2.1 on 2023-05-17 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ResetPasswordToken",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="When was this token generated"
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        db_index=True, max_length=64, unique=True, verbose_name="Key"
                    ),
                ),
                (
                    "ip_address",
                    models.GenericIPAddressField(
                        blank=True,
                        default="",
                        null=True,
                        verbose_name="The IP address of this session",
                    ),
                ),
                (
                    "user_agent",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=256,
                        verbose_name="HTTP User Agent",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="password_reset_tokens",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="The User which is associated to this password reset token",
                    ),
                ),
            ],
            options={
                "verbose_name": "Password Reset Token",
                "verbose_name_plural": "Password Reset Tokens",
            },
        ),
    ]
