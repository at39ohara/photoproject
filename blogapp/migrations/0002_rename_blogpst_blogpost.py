# Generated by Django 4.1 on 2023-10-20 04:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BlogPst",
            new_name="BlogPost",
        ),
    ]
