# Generated by Django 4.2.3 on 2023-07-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_course_cretificate_course_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='time_durstion',
            new_name='time_duration',
        ),
        migrations.AlterField(
            model_name='course',
            name='cretificate',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
