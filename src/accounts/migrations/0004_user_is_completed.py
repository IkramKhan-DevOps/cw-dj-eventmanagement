# Generated by Django 3.2.9 on 2021-11-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211114_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_completed',
            field=models.BooleanField(default=False, help_text='Shows weather the account is associated with any type'),
        ),
    ]
