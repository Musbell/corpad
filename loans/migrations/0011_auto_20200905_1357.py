# Generated by Django 3.1 on 2020-09-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0010_loan_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='commodity',
            field=models.CharField(max_length=300),
        ),
    ]
