'''
Created on Jul 9, 2015

@author: Latika
'''

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'login.views.landing_view'),
    url(r'^login/$','login.views.login_view'),
    url(r'^auth/$','login.views.auth_view'),
    url(r'^logout/$','login.views.logout_view'),
    url(r'^register/$','login.views.register_user_view'),
   
    
]
