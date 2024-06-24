# Generated by Django 5.0.6 on 2024-06-12 16:56

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('HH', 'Hiphop'), ('RNB', 'Rnb'), ('DJZ', 'Soul')], max_length=10)),
                ('year_formed', models.IntegerField(validators=[django.core.validators.MinValueValidator(2021), django.core.validators.MaxValueValidator(2024)])),
                ('biography', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('off_homepage', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='categorie',
            fields=[
                ('refcat', models.AutoField(primary_key=True, serialize=False)),
                ('numcat', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='consultation',
            fields=[
                ('Numconsulta', models.AutoField(primary_key=True, serialize=False)),
                ('motifdeconsultation', models.CharField(max_length=254)),
                ('prescripteur_consultation', models.CharField(max_length=100)),
                ('debut_signe', models.CharField(max_length=100)),
                ('signe_digestifs', models.CharField(max_length=100)),
                ('signe_extra_digestif', models.CharField(max_length=100)),
                ('signe_asso_gene', models.CharField(max_length=100)),
                ('nombredeverre_alcool', models.IntegerField(null=True)),
                ('nombrepaquettabac', models.IntegerField(null=True)),
                ('medoc_en_cours', models.CharField(max_length=253)),
                ('prise_therap_tarditionnelle', models.CharField(max_length=10)),
                ('aghbs', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('acanti_vhc', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('acanti_vhd', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('serologie_retrovi', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('transaminase', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('histoiredemaladie', models.CharField(max_length=254)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('resultat', models.CharField(max_length=254)),
                ('renseignementclinic', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='hospitalisation',
            fields=[
                ('idhospitalisation', models.AutoField(primary_key=True, serialize=False)),
                ('service', models.CharField(choices=[('gastro-entérologie', 'Gastro Enterologie'), ('chirurgie', 'Chirurgie')], max_length=100)),
                ('datehospitalisation', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='lit',
            fields=[
                ('reflit', models.AutoField(primary_key=True, serialize=False)),
                ('numlit', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='medicament',
            fields=[
                ('idmedicament', models.AutoField(primary_key=True, serialize=False)),
                ('nommedicament', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='pays',
            fields=[
                ('idpays', models.AutoField(primary_key=True, serialize=False)),
                ('nompays', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='personnel_soignant',
            fields=[
                ('refpersoignant', models.AutoField(primary_key=True, serialize=False)),
                ('mdp', models.CharField(max_length=253)),
                ('nom', models.CharField(max_length=100)),
                ('contact', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='type_personnel_soignant',
            fields=[
                ('idpersoignant', models.AutoField(primary_key=True, serialize=False)),
                ('nompersog', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='bilan_imagerie',
            fields=[
                ('numbilimg', models.AutoField(primary_key=True, serialize=False)),
                ('echographie_ou_radiograpgie', models.FileField(upload_to='uploads/')),
                ('renseignementclinique', models.CharField(max_length=254)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='bilan_biologique',
            fields=[
                ('numbilanbio', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='diagnostique',
            fields=[
                ('iddiag', models.AutoField(primary_key=True, serialize=False)),
                ('libdiag', models.CharField(max_length=254)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.consultation')),
            ],
        ),
        migrations.AddField(
            model_name='consultation',
            name='hospitalisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.hospitalisation'),
        ),
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('sold', models.BooleanField(default=False)),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(2021), django.core.validators.MaxValueValidator(2024)])),
                ('type', models.CharField(choices=[('Record', 'Disk'), ('Clothing', 'Vet'), ('Posters', 'Affiche'), ('Miscellaneous', 'Divers')], max_length=100)),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appli_web.band')),
            ],
        ),
        migrations.CreateModel(
            name='categorielit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nblit', models.PositiveIntegerField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.categorie')),
                ('lit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.lit')),
            ],
        ),
        migrations.AddField(
            model_name='categorie',
            name='se_trouver',
            field=models.ManyToManyField(through='appli_web.categorielit', to='appli_web.lit'),
        ),
        migrations.CreateModel(
            name='ordonnance',
            fields=[
                ('reford', models.AutoField(primary_key=True, serialize=False)),
                ('consulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='ordonnancemedicament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('medicament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.medicament')),
                ('ordonnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.ordonnance')),
            ],
        ),
        migrations.AddField(
            model_name='ordonnance',
            name='peut_contenir',
            field=models.ManyToManyField(through='appli_web.ordonnancemedicament', to='appli_web.medicament'),
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('idpatient', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=120)),
                ('contact1', models.PositiveIntegerField()),
                ('contact2', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('personne_a_contacter', models.CharField(max_length=100)),
                ('telephone_cpu', models.PositiveIntegerField()),
                ('date_naissance', models.DateField()),
                ('profession', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('sexe', models.CharField(choices=[('f', 'Féminin'), ('m', 'Masculin')], max_length=100)),
                ('commune', models.CharField(max_length=100)),
                ('quartier', models.CharField(max_length=100)),
                ('nationalite', models.CharField(max_length=100)),
                ('situation_matrimoniale', models.CharField(max_length=100)),
                ('nombre_enfant', models.PositiveIntegerField()),
                ('lit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appli_web.lit')),
            ],
        ),
        migrations.CreateModel(
            name='facture',
            fields=[
                ('idfact', models.AutoField(primary_key=True, serialize=False)),
                ('numerofact', models.PositiveIntegerField()),
                ('montantpaye', models.PositiveIntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.patient')),
            ],
        ),
        migrations.AddField(
            model_name='consultation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.patient'),
        ),
        migrations.CreateModel(
            name='constante',
            fields=[
                ('refconst', models.AutoField(primary_key=True, serialize=False)),
                ('poids', models.CharField(max_length=30)),
                ('taille', models.CharField(max_length=30)),
                ('temperature', models.CharField(max_length=30)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.patient')),
            ],
        ),
        migrations.CreateModel(
            name='antecedant_medical',
            fields=[
                ('refant', models.AutoField(primary_key=True, serialize=False)),
                ('dyslipidemie', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('cirrhose', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('hepatiteviraleb', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('datehepvirb', models.DateField(default=datetime.date.today)),
                ('hepatiteviralec', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('datehepvirc', models.DateField(default=datetime.date.today)),
                ('hepatiteviraled', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('datehepvird', models.DateField(default=datetime.date.today)),
                ('vaccination_vhb', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('dosevhb', models.CharField(max_length=40)),
                ('vaccination_vha', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('dosevha', models.CharField(max_length=40)),
                ('transfusion_sanguine', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=10)),
                ('datransing', models.DateField(default=datetime.date.today)),
                ('ictere', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('rapportsexuelnonprotege', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('partageobjettoilette', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('accidexposang', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('toxicomanie', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('diabete', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('hta', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('transplanhepatique', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=10)),
                ('autre', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=10)),
                ('precisionautre', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.patient')),
            ],
        ),
        migrations.CreateModel(
            name='antecedant_genecologique',
            fields=[
                ('refantgen', models.AutoField(primary_key=True, serialize=False)),
                ('datederniereregle', models.DateField(blank=True)),
                ('gestite', models.CharField(blank=True, max_length=100)),
                ('parite', models.CharField(blank=True, max_length=100)),
                ('prisecontraceptif', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('cesarienne', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('datecesarienne', models.DateField(blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.patient')),
            ],
        ),
        migrations.CreateModel(
            name='antecedant_familial',
            fields=[
                ('refantfam', models.AutoField(primary_key=True, serialize=False)),
                ('hepatie_vir_ASC', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('cirrhose_ASC', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('cpf_ASC', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('hepatie_vir_DSC', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('cirrhose_DSC', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('cpf_DSC', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('hepatie_vir_COL', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('cirrhose_COL', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('cpf_COL', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('poids', models.IntegerField(blank=True)),
                ('taille', models.IntegerField(blank=True)),
                ('imc', models.IntegerField(blank=True)),
                ('tension_art', models.IntegerField(blank=True)),
                ('pouls', models.IntegerField(blank=True)),
                ('temperature', models.IntegerField(blank=True)),
                ('conscience', models.CharField(max_length=50)),
                ('statutoms', models.CharField(max_length=50)),
                ('hippocraismdigital', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('oncleblanc', models.CharField(choices=[('o', 'oui'), ('n', 'non'), ('nsp', 'ne sait pas')], max_length=3)),
                ('autre', models.CharField(max_length=254)),
                ('ascite', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('cvc', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('splenomegalie', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('flechehepatique', models.CharField(max_length=10)),
                ('autresignephysique', models.CharField(max_length=254)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.patient')),
            ],
        ),
        migrations.CreateModel(
            name='antecedant_chirurgical',
            fields=[
                ('refantchir', models.AutoField(primary_key=True, serialize=False)),
                ('operachir', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('datoperachir', models.DateField(blank=True)),
                ('avp', models.CharField(choices=[('o', 'oui'), ('n', 'non')], max_length=1)),
                ('dateavp', models.DateField(blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.patient')),
            ],
        ),
        migrations.CreateModel(
            name='chu',
            fields=[
                ('numchu', models.AutoField(primary_key=True, serialize=False)),
                ('nomchu', models.CharField(max_length=100)),
                ('datecreation', models.DateField()),
                ('pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.pays')),
            ],
        ),
        migrations.AddField(
            model_name='consultation',
            name='personnel_soignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.personnel_soignant'),
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('refservice', models.AutoField(primary_key=True, serialize=False)),
                ('nomservice', models.CharField(choices=[('gastro-entérologie', 'Gastro Enterologie'), ('chirurgie', 'Chirurgie')], max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('chu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.chu')),
            ],
        ),
        migrations.AddField(
            model_name='personnel_soignant',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.service'),
        ),
        migrations.CreateModel(
            name='sortie',
            fields=[
                ('refsortie', models.AutoField(primary_key=True, serialize=False)),
                ('datesortie', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.patient')),
            ],
        ),
        migrations.AddField(
            model_name='personnel_soignant',
            name='type_personnel_soignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli_web.type_personnel_soignant'),
        ),
    ]
