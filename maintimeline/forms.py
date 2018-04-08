from django.forms import ModelForm
# from myapp.models import Comment
 
class EventCreate(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['created_by']

class EventUpdate(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['created_by']

class EventDelete(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['created_by']