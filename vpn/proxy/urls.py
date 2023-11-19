from django.urls import path
from .views import create_site, view_sites, update_site, proxy_view, site_detail, site_statistics

app_name = 'proxy'

urlpatterns = [
    path('create_site/', create_site, name='create_site'),
    path('view_sites/', view_sites, name='view_sites'),
    path('edit_site/<int:site_id>/', update_site, name='edit_site'),
    path('site_detail/<int:site_id>/', site_detail, name='site_detail'),
    path('site_statistics/', site_statistics, name='site_statistics'),
    path('<str:site_name>/<path:routes_on_original_site>/', proxy_view, name='proxy_view')
]