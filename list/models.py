from django.db import models
from django.contrib.auth.models import User


class Challenge(models.Model):
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    points = models.IntegerField(default=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="easy")
    created_at = models.DateTimeField(auto_now_add=True)
    flag =models.CharField(max_length=100) 
    
    def __str__(self):
        return f"{self.title} ({self.points} pts)"


class Solve(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    solved_at = models.DateTimeField(auto_now_add=True)  
    submitted_flag = models.CharField(max_length=100)
    is_correct = models.BooleanField() 
    
    def __str__(self):
        return f"{self.user} - {self.challenge} - {'Correct' if self.is_correct else 'Incorrect'}"

