# Generated by Django 4.0.3 on 2022-03-27 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0012_remove_mycourse_length_of_hous_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='sb_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userside.mycourse'),
        ),
    ]