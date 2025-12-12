from django.urls import path
from . views import ChallengeListView, ChallengeDetailView, SolveView

urlpatterns = [
   path('', ChallengeListView.as_view(), name='challenge_list'),
   path('<int:pk>/', ChallengeDetailView.as_view(), name='challenge_detail'),
#    path("solve/", SolveListView.as_view(), name="solve_list"),
   path("<int:pk>/solve/", SolveView.as_view(), name="challenge_solve"),
]