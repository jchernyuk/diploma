from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
]
