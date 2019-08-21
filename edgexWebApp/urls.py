"""edgexWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from documents.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

# ... the rest of your URLconf goes here ...
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('home/',  home, name='home'),
    path('index/', index, name='index'),
    path('create/', createPost, name='create'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('content_list', content_list, name='content_list'),
    path('post/<int:pk>', content_main, name='show'), 
    path('edit/<int:pk>', content_edit, name='content_edit'),
    path('delete/<int:pk>', content_delete, name='content_delete'),
    path('create/done', createDone, name='createDone'),

    path('edit/done/<int:pk>', done_edit, name='done_edit'),
    path('delete/done/<int:pk>', done_delete, name='done_delete'),
    
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




