# Generated by Django 5.0.1 on 2024-01-12 23:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("locataires", "0001_initial"),
        ("paiements", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="versement",
            old_name="status",
            new_name="status_validation",
        ),
        migrations.AlterUniqueTogether(
            name="versement",
            unique_together={("locataire", "date_paiement")},
        ),
    ]
