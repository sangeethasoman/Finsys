# Generated by Django 4.0.4 on 2022-11-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_purchasedebit_purchasedebit1_purchaseorder_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_statment',
            name='payments',
            field=models.FloatField(blank=True, null=True),
        ),
    ]