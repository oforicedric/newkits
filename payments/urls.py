
from django.urls import path
from django.conf import settings
from . import views
#from . import filters
from django.conf.urls.static import static
from .views import StripeView
from .views import scrape_amount
from .views import HomePageView
from .views import amountview       

from django.views.decorators.csrf import csrf_exempt


app_name="payments"
urlpatterns = [
    path('support/',StripeView.as_view(), name="stripe"),
    path('charge/',views.scrape_amount, name="charge"), # new
    path('amount/',views.amountview, name="amount"), # new
    
    #path('precharge/',views.scrape_amount, name="charge"), # new

    path('',HomePageView.as_view(), name='home'),
] 


urlpatterns += static(settings.STATIC_URL, document_root='staticfiles/')