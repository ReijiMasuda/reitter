from django.urls import path
from . import views
app_name = 'a'

urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.post, name="post"),
    path("contact/", views.contact, name="contact"),
    path('tweet/<int:tweet_id>/delete/', views.delete_tweet, name='delete_tweet'), 
    path('edit/<int:tweet_id>/', views.edit_tweet, name='edit_tweet'),
]