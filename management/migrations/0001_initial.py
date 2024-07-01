# Generated by Django 5.0.6 on 2024-06-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=12)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
    ]
