# Generated by Django 4.2.1 on 2023-05-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.SmallIntegerField(choices=[(0, 'Admin'), (1, 'Supervisor'), (2, 'Restaurant'), (3, 'Worker'), (4, 'Client')], default=4),
        ),
    ]