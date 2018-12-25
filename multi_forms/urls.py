from django.conf.urls import url

from multi_forms import views

app_name = "multi_forms"

urlpatterns = [
    url(r'^create/$', views.create, name="create"),
    url(r'^list/$', views.list, name="list"),
]