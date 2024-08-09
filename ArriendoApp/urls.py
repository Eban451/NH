from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_url'),
    path('', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('create-propiedad/', views.create_propiedad, name='create_propiedad'),
    path('profile/', views.profile, name='profile'),
    path('mis-propiedades/', views.list_propiedades, name='list_propiedades'),
    path('editar-propiedad/<int:propiedad_id>/', views.edit_propiedad, name='edit_propiedad'),
    path('list_all_propiedades/', views.list_all_propiedades, name='list_all_propiedades'),
]