# Generated by Django 3.2.5 on 2021-07-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20210718_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Died'),
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='fname', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='lname', max_length=100),
            preserve_default=False,
        ),
    ]
