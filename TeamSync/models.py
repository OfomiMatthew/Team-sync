from django.db import models

class Team(models.Model):
  key = models.CharField(max_length=50)
  
  def __str__(self):
    return self.key
  
class ItemMessage(models.Model):
  team = models.ForeignKey(Team,related_name='items',on_delete=models.CASCADE)
  user = models.CharField(max_length=255)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return self.team
  
  class Meta:
    ordering =['-created_at']
