# Generated by Django 3.2.15 on 2022-08-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items_ordered',
            new_name='dishes_ordered',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_by',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default='12-08-2022'),
        ),
    ]
