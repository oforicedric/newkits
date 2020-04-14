import django_filters
from .models import Club

class ClubFilter(django_filters.FilterSet):

    class Meta:
        model = Club
        fields = {
            'team':['icontains'],
            'league':['icontains'],
            }
    


        #add gender when ive added women