from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.models import User
from .models import Member, Phone
from .forms import MemberSignupForm, ProfileForm, PhoneForm, PhoneInlineFormSet
from allauth.account.forms import SignupForm

from django.forms import modelformset_factory, inlineformset_factory

def member_signup(request):
    if request.method == "POST":
        member_signup_form = MemberSignupForm(request.POST, request.FILES or None, instance=Member())
        phone_inline_form = PhoneInlineFormSet(request.POST, instance=Member())
        with transaction.atomic():
            if member_signup_form.is_valid() and phone_inline_form.is_valid():
                member_signup_form.save()
                phone_inline_form.save()
                return redirect('profile')
    else:
        member_signup_form = MemberSignupForm()
        phone_inline_form = PhoneInlineFormSet(instance=Member())
    return render(request, 'members/member_signup.html', {'member_signup_form' : member_signup_form, 'phone_inline_form' : phone_inline_form })

class MemberList(generic.ListView):
    model = Member
    paginate_by = 50
    template_name = 'members/member_list.html'

    def get_context_data(self, **kwargs):
        context = super(MemberList, self).get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        
        return context

class MemberDetail(generic.DetailView):
    model = Member
    template_name = 'members/member_detail.html'

@login_required
def profile(request):
    return render(request, 'members/profile.html')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES or None, instance=request.user.member)
        phone_inline_form = PhoneInlineFormSet(request.POST, instance=request.user.member)
        if profile_form.is_valid() and phone_inline_form.is_valid():
            profile_form.save()
            phone_inline_form.save()
            #profile = form.save(commit=False)
            #profile.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=user.member)
        phone_inline_form = PhoneInlineFormSet(instance=user.member)
    return render(request, 'members/edit_profile.html', {'profile_form': profile_form, 'phone_inline_form' : phone_inline_form })
