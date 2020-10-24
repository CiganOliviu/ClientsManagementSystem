from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.ClientsFeedBackPage.as_view(), name='feedback_page'),
    path('project-request/', views.ProjectsRequestPage.as_view(), name='projects_request'),
    path('messages/', views.client_messages, name='client_messages'),

    path('messages/<slug:message_slug>/', views.MessageDetail.as_view(), name='message_detail'),
]
