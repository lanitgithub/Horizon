# Generated by Django 3.0.9 on 2020-08-05 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_storage', '0026_auto_20200803_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='jmeterrawlogsfile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='jmeterrawlogsfile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='jmeterrequest',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_storage.JmeterRawLogsFile'),
        ),
    ]