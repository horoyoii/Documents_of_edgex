# Generated by Django 2.2.2 on 2019-08-24 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_post_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_main',
            field=models.CharField(max_length=40),
        ),
    ]
