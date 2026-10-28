from django.db import models
from django.conf import settings


class MoodCategory(models.Model):
    """Broad family of feelings."""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "mood categories"
        ordering = ["name"]
        
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    """Free-form context label."""
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    
    class Meta:
        ordering = ["name"]
        
    def __str__(self):
        return self.name
    
class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ("happy", "Happy"),
        ("sad", "Sad"),
        ("angry", "Angry"),
        ("anxious", "Anxious"),
        ("tired", "Tired"),
        ("calm", "Calm"),
    ]
    
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    intensity = models.IntegerField(default=5)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    category = models.ForeignKey(
        MoodCategory,
        on_delete= models.SET_NULL,
        null=True, blank=True,
        related_name="entries",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="entries"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="entries")
    
    class Meta:
        verbose_name_plural = "mood entries"
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"{self.get_mood_display()} ({self.intensity}/10) - {self.user}"