# Generated by Django 4.1.1 on 2022-09-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_author_delete_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
    ]