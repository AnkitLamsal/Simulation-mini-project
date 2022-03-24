from django.urls import path, reverse_lazy
from .views import ResultCreate, TeamCreate, TeamView, home, ResultDetailView
app_name = "sports_analytics"

urlpatterns = [
    path('create-team/',TeamCreate.as_view(), name="createTeam"),
    path("home/",home ,name='home'),
    path("view-teams/",TeamView.as_view(), name='viewTeam'),
    path('results-team/',ResultCreate.as_view(),name='simulate'),
    # path('home/<int:pk>/', home_, name='test'),
    path('simulation-details/<int:pk>/',ResultDetailView.as_view(), name="result_detail"),
]