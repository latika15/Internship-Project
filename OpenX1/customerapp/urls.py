from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views


urlpatterns = [
    
               url(r'^$', 'customerapp.views.customerHome'),
               url(r'^categories/(?P<subcategoryID>[\w\ ]+)/$', 'customerapp.views.subcategoryPage'),
               url(r'^categories/(?P<subcategoryID>[\w\ ]+)/report_issue/$', 'customerapp.views.reportIssuePage'),
               url(r'^categories/(?P<subcategoryID>[\w\ ]+)/(?P<issue>[0-9]+)/$', 'customerapp.views.followPage'), 
               url(r'^myprofile/$', 'customerapp.views.myprofilePage'),
               url(r'^mysuggestions/$', 'customerapp.views.mysuggestionsPage'),
               url(r'^suggestion/$', 'customerapp.views.suggestionPage'),
               url(r'^feed/$', 'customerapp.views.feedPage'),
               url(r'^rate/$', 'customerapp.views.rate'),
               url(r'^vote/$', 'customerapp.views.vote'),
               url(r'^vote-suggestion/$', 'customerapp.views.voteSuggestion'),
               url(r'^notifications/$', 'customerapp.views.notificationsPage'),   
               url(r'^password_change/$', views.password_change, name='password_change'),
               url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
               url(r'^issue/(?P<issueId>[0-9]+)/$', 'customerapp.views.issuePage'),
               url(r'^idea/(?P<ideaId>[0-9]+)/$', 'customerapp.views.ideaPage'),
          ]   


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)