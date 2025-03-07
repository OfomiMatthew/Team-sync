from django.conf import settings 
from django.core.mail import send_mail 
from django.utils import timezone
from datetime import timedelta
from .models import ItemMessage 

def notify_users(team,user):
  users = []
  for item in team.items.all():
    if item.user not in users:
      users.append(item.user)
  subject = f'New message in {team.key}'
  message = f'{user} wrote a new message'
  from_email = settings.DEFAULT_FROM_EMAIL
  
  send_mail(subject,message,from_email,users)
  
def remove_old_teams():
  twenty_four_hours_ago = timezone.now() - timedelta(hours=24)
  old_items = ItemMessage.objects.filter(created_at__gt=twenty_four_hours_ago)
  
  if old_items.count() == 0:
    team = old_items.first().team
    team.delete()