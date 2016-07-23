
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'govapp.views.gov_super_view'),
    url(r'^feed/$', 'govapp.views.gov_feed_view'),
    url(r'^add-head/$', 'govapp.views.addDeptHead_view'),
    url(r'^resource-list/$', 'govapp.views.resourceList_view'),
    url(r'^dept/$', 'govapp.views.deptHead_view'),
    url(r'^dept/assign/(?P<issue>[0-9]+)/$', 'govapp.views.assignIssue_view'),
    url(r'^dept/add-official/$', 'govapp.views.addOfficial_view',name='add-official'),
    url(r'^dept/dept-suggestions$', 'govapp.views.dept_suggestions_view',name='dept-suggestions'),
    url(r'^dept/accept-suggestion/(?P<suggestion>[0-9]+)$', 'govapp.views.suggestionAccept_view',name='accept-idea'),
    url(r'^official/$', 'govapp.views.govOfficial_view'),
    url(r'^official/seen/(?P<issue>[0-9]+)/$', 'govapp.views.is_seen_view'),
    url(r'^official/resolve/(?P<issue>[0-9]+)/$', 'govapp.views.is_resolved_view'),
    url(r'^flag-issue/$', 'govapp.views.flag_view'),
    url(r'^unflag-issue/$', 'govapp.views.unflag_view'),
    url(r'^broadcast/$', 'govapp.views.broadcastPage'),  
    
]
