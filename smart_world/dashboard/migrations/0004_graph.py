# Generated by Django 2.2.7 on 2019-11-27 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20191125_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
