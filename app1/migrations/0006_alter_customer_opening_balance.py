# Generated by Django 4.0.6 on 2022-10-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_paymentitems_inv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='opening_balance',
            field=models.FloatField(default=0),
        ),
    ]