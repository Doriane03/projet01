# Generated by Django 5.0.6 on 2024-07-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli_web', '0002_remove_categorie_se_trouver_lit_categorie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antecedant_familial',
            name='imc',
        ),
        migrations.RemoveField(
            model_name='antecedant_familial',
            name='poids',
        ),
        migrations.RemoveField(
            model_name='antecedant_familial',
            name='pouls',
        ),
        migrations.RemoveField(
            model_name='antecedant_familial',
            name='taille',
        ),
        migrations.RemoveField(
            model_name='antecedant_familial',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='antecedant_familial',
            name='tension_art',
        ),
        migrations.AddField(
            model_name='antecedant_medical',
            name='autre',
            field=models.CharField(choices=[('o', 'oui'), ('n', 'non')], default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constante',
            name='imc',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constante',
            name='pouls',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constante',
            name='tad',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constante',
            name='tas',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
