# Generated by Django 2.2.2 on 2019-06-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_userid', models.IntegerField(max_length=8)),
                ('int_score', models.IntegerField(max_length=1)),
                ('str_comment', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
