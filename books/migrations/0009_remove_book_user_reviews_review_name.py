# Generated by Django 4.2.7 on 2023-12-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_remove_review_user_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user_reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
