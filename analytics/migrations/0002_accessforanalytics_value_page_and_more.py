# Generated by Django 4.2.6 on 2023-10-13 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="accessforanalytics",
            name="value_page",
            field=models.CharField(
                default=django.utils.timezone.now,
                max_length=455,
                verbose_name="Valor da Página",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="accessforanalytics",
            name="page",
            field=models.CharField(
                choices=[("HOME", "HOME"), ("DETAIL", "DETAIL")],
                max_length=10,
                verbose_name="Página",
            ),
        ),
    ]
