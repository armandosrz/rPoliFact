from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'data/$', views.data, name='data'),
    url(r'model/$', views.model, name='model'),
    url(r'topic/$', views.topic, name='topic'),
    url(r'g_all/$', views.g_all, name='g_all'),
    url(r'g_bias/$', views.g_bias, name='g_bias'),
    url(r'g_confirmed/$', views.g_confirmed, name='g_confirmed'),
    url(r'g_false/$', views.g_false, name='g_false'),
    url(r'g_mostlyFalse/$', views.g_mostlyFalse, name='g_mostlyFalse'),
    url(r'g_mostlyTrue/$', views.g_mostlyTrue, name='g_mostlyTrue'),
    url(r'g_none/$', views.g_none, name='g_none'),
    url(r'g_verify/$', views.g_verify, name='g_verify'),
]
