from django.contrib import admin
from.models import Club,UserProfile

# Register your models here.
admin.site.register(Club)
admin.site.register(UserProfile)

#define the admin class
#@admin.register(Club) #registers the club model
class ClubAdmin(admin.ModelAdmin):
    list_display = ["team", "league", "gender", "pic"]


#register the admin class with associated model
