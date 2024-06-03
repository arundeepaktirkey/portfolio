# Generated by Django 5.0.4 on 2024-06-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontwebapp', '0008_alter_image_image_alter_internships_bg_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_link', models.CharField(default='#', max_length=100)),
                ('image_url', models.ImageField(upload_to='')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('descriptions', models.ManyToManyField(blank=True, to='frontwebapp.description')),
            ],
        ),
    ]