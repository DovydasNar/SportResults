from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView, MatchCreateView, statistics_view


urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('add-match/', MatchCreateView.as_view(), name='add-match'),
    path('edit-match/<int:pk>/', views.MatchUpdateView.as_view(), name='edit-match'),
    path('delete-match/<int:pk>/', views.MatchDeleteView.as_view(), name='delete-match'),
    path('statistics/', statistics_view, name='statistics'),
]