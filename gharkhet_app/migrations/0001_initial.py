# Generated by Django 4.0.6 on 2022-09-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gharkhet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='gharkhet_app/images')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
