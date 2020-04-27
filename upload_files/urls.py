from django.conf.urls import url
from upload_files import views

# app_name = 'GRAnalytics'

urlpatterns = [
    url(r'^likepost', views.cuemath_agent_performance, name='likepost'),
    url(r'^accounts/index/validation', views.validation, name='validation'),
    url(r'^reports', views.reports, name='reports'),
    url(r'^accounts/index/call_entry_and_cdr', views.TABLES.call_entry_and_cdr, name='call_entry_and_cdr'),
    url(r'^accounts/index/call_entry_not_matched', views.TABLES.call_entry_not_matched, name='call_entry_not_matched'),
    url(r'^accounts/index/cdr_not_matched', views.TABLES.cdr_not_matched, name='cdr_not_matched'),
    url(r'^accounts/index/cdr', views.TABLES.cdr, name='cdr'),
    url(r'^accounts/index/call_entry', views.TABLES.call_entry, name='call_entry'),
    url(r'^accounts/index/call_progress', views.TABLES.call_progress, name='call_progress'),
    url(r'^tables', views.TABLES, name='tables'),
    url(r'^accounts/index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register_user/', views.register_user, name='register_user'),
    url(r'^change_password/', views.change_pass, name='change_pass'),
    # url(r'^', views.login, name='login'),

]
