# Generated by Django 2.2.13 on 2020-06-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_storage', '0004_auto_20200618_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]