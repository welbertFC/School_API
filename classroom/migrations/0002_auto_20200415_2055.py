# Generated by Django 2.2.9 on 2020-04-15 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='classroom.Professor'),
        ),
    ]
