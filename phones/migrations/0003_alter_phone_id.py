# Generated by Django 4.1.7 on 2023-02-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_lte_exists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]