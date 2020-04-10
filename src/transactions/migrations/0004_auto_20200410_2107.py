# Generated by Django 2.2.2 on 2020-04-10 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200410_2107'),
        ('transactions', '0003_auto_20200410_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='requester',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='users.RequestRole'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supply',
            name='supplier',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, related_name='supplies', to='users.SupplyRole'
            ),
            preserve_default=False,
        ),
    ]
