# Generated by Django 4.1.4 on 2022-12-31 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiveapp", "0002_remove_archive_file_size_archive_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="archive",
            name="file",
        ),
        migrations.AddField(
            model_name="archive",
            name="files",
            field=models.FileField(blank=True, null=True, upload_to="files/"),
        ),
        migrations.AlterField(
            model_name="archive",
            name="filiere",
            field=models.CharField(
                choices=[
                    ("FC", "Finance & Comptabilité (FC)"),
                    ("GRH", "Gestion des Ressources Humaines (GRH)"),
                    ("BA", "Banques & Assurances (BA)"),
                    ("TCM", "Techniques Commerciales et Marketing (TCM)"),
                    ("SAE", "Statistique Appliquée á Economie (SAE)"),
                    ("DI", "Développement Informatique (DI)"),
                    ("IG", "Informatique de Gestion (IG)"),
                    ("RT", "Réseaux informatiques et Télécommunications (RT)"),
                ],
                default="FC",
                max_length=20,
            ),
        ),
    ]
