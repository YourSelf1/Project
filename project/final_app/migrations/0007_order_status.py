# Generated by Django 3.2 on 2021-05-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0006_rename_customer_order_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
