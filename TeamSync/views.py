from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import ItemMessageForm
from .utilities import notify_users


def home(request):
  return render(request,'TeamSync/home.html')

def team_sync(request):
  key = request.GET.get('key','')
  user = request.GET.get('user','')
  team,created = Team.objects.get_or_create(key=key)
  
  if created:
    messages.success(request,'The Team was created')
  if request.method == 'POST':
    form = ItemMessageForm(request.POST)
    if form.is_valid():
      item = form.save(commit=False)
      item.team = team 
      item.save()
      notify_users(team,item.user)
      
      return redirect(f'/team/?key={key}&user={user}')
  
  return render(request,'TeamSync/team.html',{'user':user,'team':team})
