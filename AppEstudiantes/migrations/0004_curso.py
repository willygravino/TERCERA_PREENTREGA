# Generated by Django 4.1.7 on 2023-03-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEstudiantes', '0003_profe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=40)),
                ('camada', models.CharField(max_length=20)),
            ],
        ),
    ]
