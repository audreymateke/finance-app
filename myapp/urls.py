from django.urls import path, include
from django.views.generic import RedirectView
from . import views  # Import your views

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=True)),  # Redirect root URL to /home/
    path('home/', views.home, name='home'),
    path('home/login/', views.user_login, name='login'),
    path('home/logout/', views.user_logout, name='logout'),  # Change name to 'logout'
    path('home/register/', views.user_register, name='register'),
    path('home/add_expences/', views.add_expences, name='add_expence'),
    path('home/delete_expences/', views.delete_expences, name='delete_expences'),
    path('home/update_expences/', views.update_expences, name='update_expences'),
    path('home/update_expences_two/', views.update_expences_two, name='update_expences_two'),
]
