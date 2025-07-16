

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('login.urls', namespace='login')),
    path('', RedirectView.as_view(pattern_name='login:login', permanent=False)),
]
