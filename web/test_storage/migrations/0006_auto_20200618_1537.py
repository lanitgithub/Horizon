# Generated by Django 2.2.13 on 2020-06-18 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_storage', '0005_auto_20200618_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True, verbose_name='Account'),
        ),
        migrations.AddField(
            model_name='project',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_storage.Account'),
        ),
    ]