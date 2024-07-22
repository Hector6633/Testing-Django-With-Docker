# Generated by Django 5.0.6 on 2024-07-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampledocker', '0005_department_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=10)),
                ('year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
                ('books', models.ManyToManyField(related_name='stores', to='sampledocker.book')),
            ],
        ),
    ]