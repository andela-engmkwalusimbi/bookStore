from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.add_books, name='add'),
    url(r'^$', views.list_books, name='list'),
]