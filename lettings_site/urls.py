from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/', include(('profiles.urls', 'profiles'))),
    path('lettings/', include(('lettings.urls', 'lettings'))),
    path('admin/', admin.site.urls),
    path('sentry-debug/', views.trigger_error)
]
