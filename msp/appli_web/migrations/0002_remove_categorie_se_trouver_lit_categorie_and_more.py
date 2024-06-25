# Generated by Django 5.0.6 on 2024-06-24 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli_web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='se_trouver',
        ),
        migrations.AddField(
            model_name='lit',
            name='categorie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appli_web.categorie'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='categorielit',
        ),
    ]
