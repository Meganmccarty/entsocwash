from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Phone, Geography, Subject, Taxonomy
from django.db import transaction
from allauth.account.forms import SignupForm, LoginForm, AddEmailForm
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit


class PhoneForm(forms.ModelForm):
    phone_number = forms.CharField(label='Phone number', max_length=255, required=False)
    phone_type = forms.CharField(label='Phone type (e.g., work)', max_length=255, required=False)
    
    class Meta:
        model = Phone
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': ''
            })

PhoneInlineFormSet = inlineformset_factory(
    Member,
    Phone,
    form=PhoneForm,
    fields=('phone_number', 'phone_type',),
    extra=1,
    can_delete=False
)

class GeographyForm(forms.ModelForm):
    geography = forms.CharField(label='Geography', max_length=255, required=False)
    
    class Meta:
        model = Geography
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super(GeographyForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': ''
            })

GeographyInlineFormSet = inlineformset_factory(
    Member,
    Geography,
    form=GeographyForm,
    fields=('geography',),
    extra=1,
    can_delete=False
)

class SubjectForm(forms.ModelForm):
    subject = forms.CharField(label='Subject', max_length=255, required=False)

    class Meta:
        model = Subject
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': ''
            })

SubjectInlineFormSet = inlineformset_factory(
    Member,
    Subject,
    form=SubjectForm,
    fields=('subject',),
    extra=1,
    can_delete=False
)

class TaxonomyForm(forms.ModelForm):
    taxon = forms.CharField(label='Taxonomy', max_length=255, required=False)

    class Meta:
        model = Taxonomy
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super(TaxonomyForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': ''
            })

TaxonomyInlineFormSet = inlineformset_factory(
    Member,
    Taxonomy,
    form=TaxonomyForm,
    fields=('taxon',),
    extra=1,
    can_delete=False
)

class MemberSignupForm(SignupForm):
    first_name = forms.CharField(label='First name', max_length=255)
    middle_name = forms.CharField(label='Middle name', max_length=255, required=False)
    last_name = forms.CharField(label='Last name', max_length=255)
    suffix = forms.CharField(label='Suffix', max_length=255, required=False)
    address1 = forms.CharField(label='Address 1', max_length=255)
    address2 = forms.CharField(label='Address 2', max_length=255, required=False)
    address3 = forms.CharField(label='Address 3', max_length=255, required=False)
    city = forms.CharField(label='City', max_length=255)
    state = forms.CharField(label='State', max_length=255)
    zip_code = forms.CharField(label='Zip code', max_length=10)
    country = forms.CharField(label='Country', max_length=255)
    lsid = forms.CharField(label='LSID', max_length=255, required=False)
    orcid = forms.CharField(label='ORCID', max_length=255, required=False)
    photo = forms.ImageField(label='Profile picture', required=False)
    url = forms.URLField(label='Website url', max_length=255, required=False)
    info_visible = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': '', 'id': 'boolean-checkbox'}),
        label='Make contact info public (leave unchecked to keep private)',
    )
    
    class Meta:
        model = Member
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'address1', 
            'address2',
            'address3',
            'city',
            'state',
            'zip_code',
            'country',
            'lsid',
            'orcid',
            'photo',
            'url',
            'info_visible',
        ]
    
    def __init__(self, *args, **kwargs):
        super(MemberSignupForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': ''
            })

    def save(self, request):
        user = super(MemberSignupForm, self).save(request)
        user.member.first_name = self.cleaned_data['first_name']
        user.member.middle_name = self.cleaned_data['middle_name']
        user.member.last_name = self.cleaned_data['last_name']
        user.member.suffix = self.cleaned_data['suffix']
        user.member.address1 = self.cleaned_data['address1']
        user.member.address2 = self.cleaned_data['address2']
        user.member.address3 = self.cleaned_data['address3']
        user.member.city = self.cleaned_data['city']
        user.member.state = self.cleaned_data['state']
        user.member.zip_code = self.cleaned_data['zip_code']
        user.member.country = self.cleaned_data['country']
        user.member.lsid = self.cleaned_data['lsid']
        user.member.orcid = self.cleaned_data['orcid']
        user.member.photo = self.cleaned_data['photo']
        user.member.url = self.cleaned_data['url']
        user.save()
        return user


class CustomLoginForm(LoginForm):
    pass

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': ''
            })


class CustomAddEmailForm(AddEmailForm):
    pass

    def __init__(self, *args, **kwargs):
        super(CustomAddEmailForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': ''
            })


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First name*', max_length=255)
    middle_name = forms.CharField(label='Middle name', max_length=255, required=False)
    last_name = forms.CharField(label='Last name*', max_length=255)
    suffix = forms.CharField(label='Suffix', max_length=255, required=False)
    address1 = forms.CharField(label='Address 1*', max_length=255)
    address2 = forms.CharField(label='Address 2', max_length=255, required=False)
    address3 = forms.CharField(label='Address 3', max_length=255, required=False)
    city = forms.CharField(label='City*', max_length=255)
    state = forms.CharField(label='State*', max_length=255)
    zip_code = forms.CharField(label='Zip code*', max_length=10)
    country = forms.CharField(label='Country*', max_length=255)
    lsid = forms.CharField(label='LSID', max_length=255, required=False)
    orcid = forms.CharField(label='ORCID', max_length=255, required=False)
    photo = forms.ImageField(label='Profile picture', required=False)
    url = forms.URLField(label='Website url', max_length=255, required=False)
    info_visible = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': '', 'id': 'boolean-checkbox'}),
        label='Make contact info public (leave unchecked to keep private)',
    )

    class Meta:
        model = Member
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'address1', 
            'address2',
            'address3',
            'city',
            'state',
            'zip_code',
            'country',
            'lsid',
            'orcid',
            'photo',
            'url',
            'info_visible',
        ]
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': ''
            })