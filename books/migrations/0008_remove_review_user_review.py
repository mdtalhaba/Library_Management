# Generated by Django 4.2.7 on 2023-12-31 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_review_user_review_user_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user_review',
        ),
    ]
