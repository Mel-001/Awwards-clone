from django.urls import path
from . import views
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    
    path('project/<int:id>',views.project,name='project'),
    path('Awwards/profile/',views.view_profile,name='view-profile'),
    path('search/', views.search_project, name='search_project'),
    path('newproject/', views.new_project, name='newproject'),
    path('Awwardsapi/api/profile/', views.ProfileList.as_view(),name='api-profile'),
    path('Awwardsapi/api/project/', views.ProjectList.as_view(),name='api-project'),
    path('Awwardsapi/',views.api_page,name='api-page'),
    # path('register/',views.register, name='register'),
    
]
