# Generated by Django 3.2.7 on 2023-02-03 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='SmsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default=0)),
                ('Sms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smss', to='mainapp.user')),
            ],
            options={
                'verbose_name': 'Sms',
                'verbose_name_plural': 'Smss',
            },
        ),
    ]
