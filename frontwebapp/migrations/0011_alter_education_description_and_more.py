# Generated by Django 5.0.4 on 2024-06-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontwebapp', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
