# Generated by Django 2.2.2 on 2020-04-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
