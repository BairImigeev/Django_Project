# Generated by Django 4.0.3 on 2022-03-15 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0004_mycourse_educator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('course', models.ManyToManyField(to='userside.mycourse')),
            ],
        ),
    ]
