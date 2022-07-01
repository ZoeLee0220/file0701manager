# Generated by Django 4.0.3 on 2022-06-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='papers',
            name='basement_message',
            field=models.CharField(max_length=100, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='papers',
            name='title',
            field=models.CharField(max_length=100, verbose_name='文献名称'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='SCIE_choice',
            field=models.CharField(choices=[('SCI', 'SCI'), ('IE', 'IEEE'), ('SCIE', 'SCI&IEEE'), ('None', 'ALL NOT')], max_length=20),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='name',
            field=models.CharField(max_length=100, verbose_name='期刊名称'),
        ),
    ]