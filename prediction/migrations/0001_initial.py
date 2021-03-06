# Generated by Django 3.1.4 on 2021-01-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=20)),
                ('championId', models.CharField(max_length=20)),
                ('key', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('blurb', models.CharField(max_length=1000)),
                ('info', models.JSONField()),
                ('image', models.JSONField()),
                ('tags', models.CharField(max_length=100)),
                ('partype', models.CharField(max_length=20)),
                ('stats', models.JSONField()),
            ],
        ),
    ]
