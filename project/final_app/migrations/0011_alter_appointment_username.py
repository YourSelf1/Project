# Generated by Django 3.2 on 2021-05-13 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('final_app', '0010_rename_message_appointment_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
