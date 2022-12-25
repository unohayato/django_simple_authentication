from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login')
]