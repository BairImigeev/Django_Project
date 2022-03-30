# Generated by Django 4.0.3 on 2022-03-25 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0009_alter_course_options_alter_educator_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseInstanse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_begin', models.DateField(verbose_name='Дата начала')),
                ('date_end', models.DateField(verbose_name='Дата окончания')),
                ('length_of_hous', models.FloatField(blank=True, null=True, verbose_name='вещ: Количество часов в день')),
                ('length_of_week', models.IntegerField(blank=True, null=True, verbose_name='Количество дней в неделю')),
            ],
            options={
                'verbose_name': 'Mой Курс',
                'verbose_name_plural': 'Мои Курсы',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='course',
            name='action_object',
        ),
        migrations.RemoveField(
            model_name='course',
            name='date_begin',
        ),
        migrations.RemoveField(
            model_name='course',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='course',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='course',
            name='status',
        ),
        migrations.AddField(
            model_name='course',
            name='length_of_month',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество месяцев'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='courseinstanse',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userside.course'),
        ),
    ]
