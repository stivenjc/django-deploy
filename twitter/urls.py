from django.urls import path

from twitter.views import home, DeletePost, profile, edit_profile

app_name = 'twitter'

urlpatterns = [
    path('', home, name='home'),
    path('deletepost/<int:pk>/', DeletePost.as_view(), name='delete-post'),
    path('profile/<str:username>/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit-profile'),
]
