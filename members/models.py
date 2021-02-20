from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail.admin.edit_handlers import InlinePanel

class Member(models.Model):

    member_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    middle_name = models.CharField(max_length=255, default='', null=True, blank=True)
    suffix = models.CharField(max_length=255, default='', null=True, blank=True)
    lsid = models.CharField(max_length=255, null=True, blank=True)
    orcid = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    address3 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="profile_photos", null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    info_visible = models.BooleanField(default=False)
    notes = models.TextField(max_length=2000, null=True, blank=True)

    InlinePanel('member_phone', label="Phone numbers")

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def get_username(self):
        return self.user.username
    
    def get_email(self):
        return self.user.email

    def save(self, *args, **kwargs):
       super().save(*args, **kwargs)

def member_receiver(sender, instance, created, *args, **kwargs):
    if created:
        member = Member.objects.create(user=instance)
    else:
        instance.member.save()

post_save.connect(member_receiver, sender=User)

class Phone(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='has_phones')
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=10)

    def __str__(self):
        return self.phone_number

class Geography(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='has_geographies')
    geography = models.CharField(max_length=255)
    
    def __str__(self):
        return self.geography

class Subject(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='has_subjects')
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.subject

class Taxonomy(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='has_taxons')
    taxon = models.CharField(max_length=255)

    def __str__(self):
        return self.taxon
