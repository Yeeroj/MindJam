# Generated by Django 3.0.3 on 2020-06-02 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Healthy', '0002_auto_20200602_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='area',
            field=models.CharField(max_length=100, null=True),
        ),
    ]