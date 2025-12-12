from django.contrib import admin
from list.models import Challenge, Solve

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('DIFFICULTY_CHOICES', 'title',  'description', 'points', 'difficulty', 'created_at')

class SolveAdmin(admin.ModelAdmin):
     list_display =('user', 'challenge', 'solved_at', 'submitted_flag')
    
admin.site.register(Challenge,ChallengeAdmin)
admin.site.register(Solve,SolveAdmin)