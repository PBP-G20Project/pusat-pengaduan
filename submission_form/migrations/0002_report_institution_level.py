# Generated by Django 4.1 on 2022-10-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='institution_level',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
