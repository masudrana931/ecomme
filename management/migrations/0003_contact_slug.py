# Generated by Django 5.0.6 on 2024-07-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_contact_created_at_contact_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
