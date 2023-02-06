from django.urls import path, include
from .views import project_detail, project_list, projectlist, ProjectCreateView, ProjectCreateView, home
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    # path('', indextwo, name='indextwo'),
    path('project_list', projectlist.as_view(), name='list'),
    path('project_list', project_list, name='list'),
    # path('testing', testing, name='testing'),
    path('add', ProjectCreateView.as_view(), name='add'),
    # path('add/', ProjectCreateView, name='add'),
    path('slug=<slug:project_slug>', project_detail, name='detail'),
    # path("user_list/", User_List.as_view(), name="user_list"),
]