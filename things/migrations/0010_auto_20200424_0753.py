# Generated by Django 3.0 on 2020-04-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0009_auto_20200424_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playersgame',
            name='firstblood',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='playersgame',
            name='firstblood_die',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]