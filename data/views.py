from django.shortcuts import render,redirect
from .models import Club,UserProfile
from datetime import timezone, datetime
from django.views.generic import ListView, DetailView
import os
import shutil

import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup
from .filters import ClubFilter

def clubfilter(request):
    theclubs = Club.objects.all()
    return render(request,"/",locals())

class ClubListView(ListView):
    model = Club
    template_name = "data/newkit.html"
   # return render(request,"news/")

 
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ClubFilter(self.request.GET, queryset=self.get_queryset())
        return context

    
def scrape(request):

    user_p = UserProfile.objects.filter(user=request.user).first()
    #user_p.last_scrape = datetime.now(timezone.utc)
    user_p.save()

    session = requests.Session()
    session.headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    url= "https://www.footballwebpages.co.uk/league-one"
    
    content = session.get(url,verify=False).content #grabs the html

    soup = BeautifulSoup(content,"html.parser")

    rows = soup.find_all('tr')#returns a list
   # pic_row = soup.find_all
    for i in rows:
        if 'title' in i.attrs:
            teams = i['title']
            for pic in i.find_all('img'):
                url = "https://www.footballwebpages.co.uk/league-one" + pic.get('data-src') 
            
               # stackoverflow solution
                media_root = '\\django_projects\\Newkit\\media_root'
                if not url.startswith(("data:image", "javascript")):
                    local_filename = url.split('/')[-1].split("?")[0]
                    r = session.get(url, stream=True, verify=False)
                    with open(local_filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024):
                            f.write(chunk)
                            f.flush()

                    current_image_absolute_path = os.path.abspath(local_filename)
                    shutil.move(current_image_absolute_path, media_root)

                new_club =Club()
                new_club.team = teams
              #  new_club.pic = local_filename
                new_club.league = "SkyBet League 1"
           #     new_club.gender = "male"
                new_club.save()
              
    return redirect('/newkits')
# club,league,pic,gender in a table

def payment (request):
    return redirect('/payments/support')
