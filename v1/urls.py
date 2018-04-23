from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit$', views.SubmitStory.as_view()),
    url(r'^list$', views.GetStoryList.as_view()),
]