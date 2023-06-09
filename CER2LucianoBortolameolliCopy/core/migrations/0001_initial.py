# Generated by Django 4.2 on 2023-06-08 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('Nombre_Categ', models.CharField(max_length=87, primary_key=True, serialize=False)),
                ('Desc_Categ', models.CharField(max_length=434)),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('ID_Correl_Com', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Titulo_Com', models.CharField(max_length=87)),
                ('Mensaje_Com', models.CharField(max_length=434)),
                ('Fecha_Env_Com', models.DateTimeField(auto_now_add=True)),
                ('Fecha_Mod_Com', models.DateTimeField(auto_now=True)),
                ('Curso_Choice_Com', models.CharField(choices=[('C_Gen', 'General'), ('C_Pre', 'Preescolar'), ('C_Bas', 'Basica'), ('C_Med', 'Media')], default='C_Gen', max_length=20)),
                ('Categ_Com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
