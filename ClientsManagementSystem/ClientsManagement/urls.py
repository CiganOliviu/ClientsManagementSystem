from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('home/', views.index, name='index'),
    path('feedback/', views.ClientsFeedBackPage.as_view(), name='feedback_page'),
    path('project-request/', views.ProjectsRequestPage.as_view(), name='projects_request'),
    path('messages/', views.client_messages, name='client_messages'),

    path('messages/<slug:message_slug>/', views.MessageDetail.as_view(), name='message_detail'),

]
