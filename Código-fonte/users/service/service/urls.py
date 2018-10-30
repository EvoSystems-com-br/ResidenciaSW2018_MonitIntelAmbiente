
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^docs/', include_docs_urls(title='User API', description='RESTful API for User')),
    url(r'^', include(('users_service.urls', 'users'), namespace='users')),
]