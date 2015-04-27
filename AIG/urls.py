from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'AIG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cFoodQuiz/', include('cFoodQuiz.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
