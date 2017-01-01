from django.conf.urls import url

from registration import views

urlpatterns = [
    url(r'^registration/$', view=views.registration, name='register'),
    url(r'^registration/success', view=views.success_registration, name='success_registration')
]