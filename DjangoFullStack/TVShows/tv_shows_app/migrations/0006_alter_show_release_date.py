# Generated by Django 4.1.1 on 2022-10-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0005_alter_show_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
