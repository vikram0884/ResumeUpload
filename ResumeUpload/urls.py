"""ResumeUpload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from su import views as su_views
from anyuser import views as au_views

urlpatterns = [
    # DJango admin page for user addition, assign permission etc...
    url(r'^admin/', admin.site.urls),

    #ADMIN urls for login, logout, list of action items, view application, approve application & reject application
    url(r'^su/login/', auth_views.login),
    url(r'^su/logout/', auth_views.logout),
    url(r'^su/list/', su_views.view_files),
    url(r'^su/view*', su_views.view_doc),
    url(r'^su/approve*', su_views.approve_doc),
    url(r'^su/reject*', su_views.reject_doc),

    #Applicant url for upload, upload.do is an internal url in upload form
    url(r'^upload/', au_views.upload_page),
    url(r'^upload.do', au_views.upload_file),

]