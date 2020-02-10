# Generated by Django 2.2.9 on 2020-02-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200201_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_pro',
            field=models.BooleanField(default=False, help_text='Can access articles for pro / プロユーザ'),
        ),
    ]
