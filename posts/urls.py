from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static



app_name="posts"
urlpatterns = [
             #   path("")
] 


urlpatterns += static(settings.STATIC_URL, document_root='static/')