# models.py
from django.db import models
from django.utils import timezone

class Notification(models.Model):
    TYPE_CHOICES = [
        ('success', 'Félicitations'),
        ('warning', 'Alerte'),
        ('info', 'Information'),
        ('danger', 'Danger'),
    ]
    
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def time_display(self):
        """Retourne l'affichage formaté du temps (Maintenant, Il y a X minutes, etc.)"""
        now = timezone.now()
        diff = now - self.created_at
        
        if diff.days == 0:
            if diff.seconds < 60:
                return "Maintenant"
            elif diff.seconds < 3600:
                minutes = diff.seconds // 60
                return f"Il y a {minutes} minute{'s' if minutes > 1 else ''}"
            else:
                return self.created_at.strftime("%H:%M")
        elif diff.days == 1:
            return "Hier"
        else:
            return self.created_at.strftime("%d/%m/%Y")

class Device(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    energy_consumption = models.FloatField()  # en kWh
    active_since = models.DateTimeField()
    percentage_change = models.FloatField(default=0)  # pourcentage de changement
    
    def __str__(self):
        return f"{self.name} ({self.location})"