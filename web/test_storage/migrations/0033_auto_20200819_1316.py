# Generated by Django 3.0.8 on 2020-08-19 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_storage', '0032_auto_20200812_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='testplan',
            name='load_stations',
            field=models.ManyToManyField(help_text='Указываем только станции с которых ПЛАНИРУЕМ подавать нагрузкау', to='test_storage.LoadStation', verbose_name='Список станций'),
        ),
        migrations.AlterField(
            model_name='jmeterrequest',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_storage.JmeterRawLogsFile'),
        ),
        migrations.AlterField(
            model_name='loadstation',
            name='memory_size',
            field=models.FloatField(blank=True, null=True, verbose_name='Оflower==0.9.5бъём памяти, Гб'),
        ),
        migrations.AlterField(
            model_name='test',
            name='load_stations',
            field=models.ManyToManyField(help_text='Указываем только станции с которых ФАКТИЧЕСКИ подавалась нагрузка.', to='test_storage.LoadStation', verbose_name='Список станций'),
        ),
    ]
