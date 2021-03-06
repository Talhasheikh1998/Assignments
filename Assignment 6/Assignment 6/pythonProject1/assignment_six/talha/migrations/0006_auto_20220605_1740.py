# Generated by Django 3.2.13 on 2022-06-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanzla', '0005_auto_20220605_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='studentprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(blank=True, default='img.png', null=True, upload_to='images')),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='account',
        ),
        migrations.DeleteModel(
            name='basic',
        ),
    ]
