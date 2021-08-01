# Generated by Django 3.1.7 on 2021-06-04 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_equipamento', models.CharField(max_length=100)),
                ('nome_display', models.CharField(max_length=100)),
                ('idsectra', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='RevisaoManuais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ns_min', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='manuais/pdf')),
                ('nome_equipamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='manuais', to='manuais.equipamentos')),
            ],
        ),
    ]