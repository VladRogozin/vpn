from django.urls import path
from .views import register, user_login, user_logout, update_profile, detail_profile

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('edit_profile/', update_profile, name='edit_profile'),
    path('detail_profile/', detail_profile, name='detail_profile'),

]
