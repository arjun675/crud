# Generated by Django 4.1.2 on 2022-11-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('salary', models.IntegerField()),
                ('dsg', models.CharField(max_length=20)),
                ('city', models.CharField(blank=True, default='Noida', max_length=20, null=True)),
                ('state', models.CharField(blank=True, default='UP', max_length=20, null=True)),
            ],
        ),
    ]
