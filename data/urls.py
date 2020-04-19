
from django.urls import path
from django.conf import settings
from . import views
from . import filters
from django.conf.urls.static import static
from .views import ClubListView


app_name="data"
urlpatterns = [
    path('payments/',views.payment, name="payments")
] 


urlpatterns += static(settings.STATIC_URL, document_root='staticfiles/')