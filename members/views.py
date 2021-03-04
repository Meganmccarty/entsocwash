from allauth.account.utils import complete_signup
from allauth.account.views import SignupView
from allauth.exceptions import ImmediateHttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.models import User
from .models import Member, Phone
from .forms import (
    MemberSignupForm,
    ProfileForm,
    PhoneForm,
    PhoneInlineFormSet,
    GeographyForm,
    GeographyInlineFormSet,
    SubjectForm,
    SubjectInlineFormSet,
    TaxonomyForm,
    TaxonomyInlineFormSet,
)
from allauth.account.forms import SignupForm
from django.forms import modelformset_factory, inlineformset_factory


class MemberSignupView(SignupView):
    """
    Member signup view
    Override the base allauth SignupView to add support for the inline phone form.
    """

    def form_valid(self, form):
        """
        Override the base allauth SignupView method so that the user is only saved once
        """
        # self.user defined in post method
        try:
            return complete_signup(
                self.request,
                self.user,
                settings.ACCOUNT_EMAIL_VERIFICATION,
                self.get_success_url(),
            )
        except ImmediateHttpResponse as e:
            return e.response

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests: instantiate empty form instances and pass to template
        """
        member_signup_form = MemberSignupForm()
        phone_inline_form = PhoneInlineFormSet(instance=Member())
        geography_inline_form = GeographyInlineFormSet(instance=Member())
        subject_inline_form = SubjectInlineFormSet(instance=Member())
        taxonomy_inline_form = TaxonomyInlineFormSet(instance=Member())
        return render(request, 'members/member_signup.html',
                      {'member_signup_form': member_signup_form,
                       'phone_inline_form': phone_inline_form,
                       'geography_inline_form': geography_inline_form,
                       'subject_inline_form': subject_inline_form,
                       'taxonomy_inline_form': taxonomy_inline_form}
                      )

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        member_form = self.get_form()
        phone_inline_form = PhoneInlineFormSet(request.POST, instance=Member())
        geography_inline_form = GeographyInlineFormSet(request.POST, instance=Member())
        subject_inline_form = SubjectInlineFormSet(request.POST, instance=Member())
        taxonomy_inline_form = TaxonomyInlineFormSet(request.POST, instance=Member())

        # TODO: add graceful error handling here. What should the user see if these db saves fail?
        with transaction.atomic():
            if member_form.is_valid() and phone_inline_form.is_valid() and geography_inline_form.is_valid() and subject_inline_form.is_valid() and taxonomy_inline_form.is_valid():
                
                self.user = member_form.save(self.request)

                # add the inline data
                phone_inline_form.instance = self.user.member
                phone_inline_form.save()
                geography_inline_form.instance = self.user.member
                geography_inline_form.save()
                subject_inline_form.instance = self.user.member
                subject_inline_form.save()
                taxonomy_inline_form.instance = self.user.member
                taxonomy_inline_form.save()

                # this does not save the user again as part of other steps
                return self.form_valid(member_form)

            else:
                # handle any error dicts and return to caller
                return render(request, 'members/member_signup.html',
                              {'member_signup_form': member_form,
                               'phone_inline_form': phone_inline_form,
                               'geography_inline_form': geography_inline_form,
                               'subject_inline_form': subject_inline_form,
                               'taxonomy_inline_form': taxonomy_inline_form}
                              )


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
        geography_inline_form = GeographyInlineFormSet(request.POST, instance=request.user.member)
        subject_inline_form = SubjectInlineFormSet(request.POST, instance=request.user.member)
        taxonomy_inline_form = TaxonomyInlineFormSet(request.POST, instance=request.user.member)
        if profile_form.is_valid() and phone_inline_form.is_valid() and geography_inline_form.is_valid() and subject_inline_form.is_valid() and taxonomy_inline_form.is_valid():
            profile_form.save()
            phone_inline_form.save()
            geography_inline_form.save()
            subject_inline_form.save()
            taxonomy_inline_form.save()
            #profile = form.save(commit=False)
            #profile.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=user.member)
        phone_inline_form = PhoneInlineFormSet(instance=user.member)
        geography_inline_form = GeographyInlineFormSet(instance=user.member)
        subject_inline_form = SubjectInlineFormSet(instance=user.member)
        taxonomy_inline_form = TaxonomyInlineFormSet(instance=user.member)
    return render(request, 'members/edit_profile.html',
                    {'profile_form': profile_form,
                    'phone_inline_form': phone_inline_form,
                    'geography_inline_form': geography_inline_form,
                    'subject_inline_form': subject_inline_form,
                    'taxonomy_inline_form': taxonomy_inline_form,}
                )
