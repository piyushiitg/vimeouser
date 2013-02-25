from django.conf.urls.defaults import patterns, include, url
from vimeocrawl import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',(r'^$', views.user_search),
(r'^search/$',views.search),
)
