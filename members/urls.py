from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.page_does_not_exist, name='page-does-not-exist'),
    path('email/', views.page_does_not_exist, name='page-does-not-exist'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('member-signup/', views.MemberSignupView.as_view(), name='member-signup'),
    path('membership-directory/', views.MemberDirectory.as_view(), name='membership-directory'),
    path('membership-gallery/', views.MemberGallery.as_view(), name='membership-gallery'),
    path('member-profile/<slug:slug>', views.MemberDetail.as_view(), name='member-profile'),
]