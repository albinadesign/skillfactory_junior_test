# Generated by Django 4.2.1 on 2023-05-18 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_text_wordcount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Text',
        ),
    ]
