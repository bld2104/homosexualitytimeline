from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from allauth.account.models import EmailAddress
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE,)
 
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
 
    class Meta:
        db_table = 'user_profile'
 
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False
 
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])



class Event(models.Model):
    created_by = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE,)
    category = models.TextField(
        null=True,
        blank=True,
    )
    headline = models.TextField()
    city = models.TextField(
        null=True,
        blank=True,
    )
    state = models.TextField(
        null=True,
        blank=True,
    )
    country = models.TextField(
        null=True,
        blank=True,
    )
    latitude = models.DecimalField(
        null=True,
        blank=True,
        max_digits=9, 
        decimal_places=6
    )
    longitude = models.DecimalField(
        null=True,
        blank=True,
        max_digits=9, 
        decimal_places=6
    )
    is_general = models.NullBooleanField()
    date = models.DateField(
        null=True,
        blank=True,)
    description = models.TextField(
        null=True,
        blank=True,
    )
    image1 = models.ImageField(
        null=True,
        blank=True,
    )
    image2 = models.ImageField(
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    @property
    def image_url(self):
        if self.image1 and hasattr(self.image1, 'url'):
            return self.image1.url
