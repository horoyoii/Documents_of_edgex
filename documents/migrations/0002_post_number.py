# Generated by Django 2.2.2 on 2019-07-09 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
