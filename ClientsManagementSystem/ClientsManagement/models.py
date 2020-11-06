from django.db import models
from django.contrib.auth.models import User

TYPE_OF_APPS = (
    ("Presentation WebSite", "Presentation WebSite"),
    ("WebApp", "Webapp"),
    ("Mobile App", "Mobile App"),
    ("Marketing Project", "Marketing Project")
)

SIZE_OF_CLIENT = (
    ("Small Client", "Small Client"),
    ("Medium Client", "Medium Client"),
    ("Big Client", "Big Client"),
    ("Huge Client", "Huge Client"),
)

TYPE_OF_CLIENT = (
    ("Self-employed Person", "Self-employed Person"),
    ("StartUp", "StartUp"),
    ("Company", "Company"),
    ("Corporation", "Corporation"),
)

PROJECT_STATUS = (
    ("Waiting for Response", "Waiting for Response"),
    ("Refused", "Refused"),
    ("Accepted", "Accepted"),
)

TYPE_OF_MESSAGE = (
    ("Projects Reference", "Projects Reference"),
    ("Workflow Reference", "Workflow Reference"),
    ("Others", "Others"),
)


class ClientsDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    size_of_client = models.CharField(max_length=100, choices=SIZE_OF_CLIENT, default="Small Client")
    type_of_client = models.CharField(max_length=100, choices=TYPE_OF_CLIENT, default="Self-employed Person")
    number_of_finished_projects = models.IntegerField(default=0)
    number_of_proposed_projects = models.IntegerField(default=0)
    number_of_projects_in_progress = models.IntegerField(default=0)
    number_of_planned_projects = models.IntegerField(default=0)

    profile_image = models.ImageField(upload_to='clients-profile-images/', default='default.jpg')

    def __str__(self):

        return str(self.user)


class ClientsFeedBack(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title


class ProjectsRequest(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    list_of_functionalities = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_OF_APPS)
    project_status = models.CharField(max_length=100, choices=PROJECT_STATUS, default="Processing")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):

        return self.project_name


class MessagesToClient(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, default='')
    message = models.TextField()
    type_of_message = models.CharField(max_length=100, choices=TYPE_OF_MESSAGE, default="Others")
    date = models.DateTimeField(auto_now_add=True)

    message_slug = models.SlugField(max_length=200, unique=True, default="")

    class Meta:
        ordering = ['-date']

    def __str__(self):

        return self.title
