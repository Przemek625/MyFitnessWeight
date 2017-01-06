from django.conf.urls import url

from login import views

urlpatterns = [
    url(r'^login/$', view=views.process_login, name='process_login'),
    ]