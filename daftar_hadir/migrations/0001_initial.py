# Generated by Django 5.1.1 on 2024-10-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='daftar_hadir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('tgl_kunjungan', models.DateField(blank=True)),
            ],
        ),
    ]
