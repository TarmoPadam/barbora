# Generated by Django 4.2.7 on 2023-11-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_of_items',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
