# Generated by Django 4.1.5 on 2023-05-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phonenumber',
            field=models.CharField(max_length=10),
        ),
    ]
