from django.conf.urls import url
from upload_files import views

# app_name = 'GRAnalytics'

urlpatterns = [
    url(r'^validation', views.validation, name='validation'),
    url(r'^graphs/', views.graphs, name='graphs'),
    url(r'^call_entry_and_cdr', views.TABLES.call_entry_and_cdr, name='call_entry_and_cdr'),
    url(r'^call_entry_not_matched', views.TABLES.call_entry_not_matched, name='call_entry_not_matched'),
    url(r'^cdr_not_matched', views.TABLES.cdr_not_matched, name='cdr_not_matched'),
    url(r'^cdr', views.TABLES.cdr, name='cdr'),
    url(r'^call_entry', views.TABLES.call_entry, name='call_entry'),
    url(r'^call_progress', views.TABLES.call_progress, name='call_progress'),
    url(r'^tables', views.TABLES,name='tables'),
    url(r'^', views.index, name='index'),
]
