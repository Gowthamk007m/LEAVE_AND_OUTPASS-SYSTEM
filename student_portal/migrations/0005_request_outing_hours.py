# Generated by Django 3.1.13 on 2023-04-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0004_request_sys_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='outing_hours',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
