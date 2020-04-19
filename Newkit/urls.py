"""Newkit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from data.views import scrape,clubfilter,ClubListView
from payments import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/',include('payments.urls',namespace="payments")),
    path('home/', include('data.urls', namespace ="data")),
    path('posts/', include('posts.urls', namespace ="posts")),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('scrape/',views.scrape, name="scrapee"),
    path('newkits/',ClubListView.as_view())

]


urlpatterns += static(settings.STATIC_URL, document_root='staticfiles/')
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Use static() to add url mapping to serve static files during development (only)
