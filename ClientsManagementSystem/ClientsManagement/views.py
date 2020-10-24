from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from ClientsManagement.models import (
    ClientsFeedBack,
    ProjectsRequest,
    MessagesToClient,
)

from .forms import (
    ClientsFeedBackForm,
    ProjectsRequestForm,
)


@login_required
def index(request):
    template_name = 'views/client_index_view.html'

    return render(request, template_name)


class ClientsFeedBackPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'views/clients_feedback/feedback.html'
    final_template_name = 'views/clients_feedback/feedback_final.html'

    def get(self, request):

        form = ClientsFeedBackForm()
        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if database_name.objects.filter(user=database_object.user, title=database_object.title,
                                        content=database_object.content).exists():
            return False

        return True

    def post(self, request):

        form = ClientsFeedBackForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user

            if self._validate_save(ClientsFeedBack, post):
                post.save()

        return render(request, self.final_template_name)


class ProjectsRequestPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'views/projects_requests/project_request_perform.html'
    final_template_name = 'views/projects_requests/project_request_perform_done.html'

    def get(self, request):

        form = ProjectsRequestForm()
        post = form.save(commit=False)

        args = {'form': form}

        return render(request, self.template_name, args)

    def _validate_save(self, database_name, database_object):

        if database_name.objects.filter(user=database_object.user, project_name=database_object.project_name,
                                        project_description=database_object.project_description,
                                        list_of_functionalities=database_object.list_of_functionalities,
                                        type=database_object.type).exists():
            return False

        return True

    def post(self, request):

        form = ProjectsRequestForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user

            if self._validate_save(ProjectsRequest, post):
                post.save()

        return render(request, self.final_template_name)


@login_required()
def client_messages(request):

    template_name = 'views/client_messages/messages_page.html'

    messages_query = MessagesToClient.objects.filter(user=request.user)

    args = {'messages_query': messages_query}

    return render(request, template_name, args)


class MessageDetail(generic.DetailView):

    model = MessagesToClient

    template_name = 'views/client_messages/message_detail.html'

    slug_field = 'message_slug'
    slug_url_kwarg = 'message_slug'
