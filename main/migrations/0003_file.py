# Generated by Django 2.0.13 on 2019-05-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190513_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('remark', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
