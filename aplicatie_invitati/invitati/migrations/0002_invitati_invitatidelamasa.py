# Generated by Django 4.1.3 on 2023-02-23 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitati', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitati',
            name='invitatidelamasa',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
