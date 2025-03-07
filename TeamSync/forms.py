from django.forms import ModelForm

from .models import ItemMessage

class ItemMessageForm(ModelForm):
  class Meta:
    model = ItemMessage
    fields = ['content','user']