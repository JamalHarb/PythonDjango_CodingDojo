# Generated by Django 4.1.1 on 2022-10-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0003_alter_show_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
