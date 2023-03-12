# Generated by Django 4.1.5 on 2023-03-12 02:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_proadditional'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProAdditional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ent', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Seuls les chiffres entre 0 et 9 sont autorisés.')], verbose_name="Numero d'entreprise")),
                ('nom_ent', models.CharField(blank=True, max_length=100, verbose_name="Nom d'entreprise")),
                ('categorie', models.CharField(blank=True, help_text='entreprise categorie', max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Seuls les caractères alphanumériques sont autorisés.')])),
                ('address', models.CharField(blank=True, max_length=100, verbose_name="le lieu de l'entreprise")),
                ('justification', models.FileField(blank=True, upload_to='media/pro_justification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
