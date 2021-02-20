from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('member-signup/', views.member_signup, name='member-signup'),
    path('membership-directory/', views.MemberList.as_view(), name='membership-directory'),
    path('member-profile/<str:pk>', views.MemberDetail.as_view(), name='member-profile'),
]