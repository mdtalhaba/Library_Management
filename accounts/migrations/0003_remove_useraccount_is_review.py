# Generated by Django 4.2.7 on 2023-12-31 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_is_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='is_review',
        ),
    ]