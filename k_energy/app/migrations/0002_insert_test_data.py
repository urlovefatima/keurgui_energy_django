# migrations/0002_insert_test_data.py
from django.db import migrations
from django.utils import timezone
import datetime

def create_test_data(apps, schema_editor):
    # Import des modèles via le registry des apps
    Notification = apps.get_model('app', 'Notification')
    Device = apps.get_model('app', 'Device')
    
    # Données pour les notifications
    notifications = [
        {
            'type': 'success',
            'title': 'Félicitations!',
            'message': 'Vous avez économisé 10 kWh cette semaine par rapport à la semaine dernière',
            'created_at': timezone.now()
        },
        {
            'type': 'warning',
            'title': 'Alerte!',
            'message': 'Votre appareil [Nom de l\'appareil] semble consommer plus que d\'habitude. Vérifiez s\'il fonctionne correctement',
            'created_at': timezone.now() - datetime.timedelta(minutes=4)
        },
        {
            'type': 'info',
            'title': 'Profitez en Fallout!',
            'message': 'L\'heure creuse commence dans 30 minutes. C\'est le moment idéal pour utiliser vos appareils gourmands en énergie',
            'created_at': timezone.now() - datetime.timedelta(hours=2)
        },
        {
            'type': 'danger',
            'title': 'Pointe de consommation détectée!',
            'message': 'Votre pic de consommation a atteint un niveau élevé aujourd\'hui. Essayez de réduire l\'utilisation des appareils gourmands en énergie.',
            'created_at': timezone.now() - datetime.timedelta(hours=1)
        },
        {
            'type': 'info',
            'title': 'Météo et énergie',
            'message': 'Une vague de froid est prévue cette semaine. Pensez à optimiser votre chauffage!',
            'created_at': timezone.now() - datetime.timedelta(days=1)
        }
    ]
    
    for notification_data in notifications:
        Notification.objects.create(**notification_data)
    
    # Données pour les appareils
    devices = [
        {
            'name': 'Climatiseur (1)',
            'location': 'salon',
            'energy_consumption': 20,
            'active_since': timezone.now() - datetime.timedelta(hours=10),
            'percentage_change': 0
        },
        {
            'name': 'Réfrigérateur',
            'location': 'salon',
            'energy_consumption': 5,
            'active_since': timezone.now() - datetime.timedelta(hours=10),
            'percentage_change': -2
        },
        {
            'name': 'Micro-onde',
            'location': 'salon',
            'energy_consumption': 20,
            'active_since': timezone.now() - datetime.timedelta(hours=10),
            'percentage_change': 0
        },
        {
            'name': 'Climatiseur (2)',
            'location': 'salon',
            'energy_consumption': 20,
            'active_since': timezone.now() - datetime.timedelta(hours=10),
            'percentage_change': 0
        },
        {
            'name': 'Micro-onde',
            'location': 'cuisine',
            'energy_consumption': 20,
            'active_since': timezone.now() - datetime.timedelta(hours=10),
            'percentage_change': 0
        },
        {
            'name': 'Télévision',
            'location': 'salon',
            'energy_consumption': 5,
            'active_since': timezone.now() - datetime.timedelta(hours=10),
            'percentage_change': -2
        },
        {
            'name': 'Ordinateur',
            'location': 'bureau',
            'energy_consumption': 8,
            'active_since': timezone.now() - datetime.timedelta(hours=8),
            'percentage_change': 1
        },
        {
            'name': 'Ordinateur',
            'location': 'salon',
            'energy_consumption': 8,
            'active_since': timezone.now() - datetime.timedelta(hours=8),
            'percentage_change': 1
        }
    ]
    
    for device_data in devices:
        Device.objects.create(**device_data)

def remove_test_data(apps, schema_editor):
    # Supprimer toutes les données si la migration est annulée
    Notification = apps.get_model('app', 'Notification')
    Device = apps.get_model('app', 'Device')
    Notification.objects.all().delete()
    Device.objects.all().delete()

class Migration(migrations.Migration):
    # Cette migration dépend de la migration initiale qui a créé les modèles
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_test_data, remove_test_data),
    ]
