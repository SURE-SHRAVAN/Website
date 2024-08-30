
from django.contrib import admin
from django.urls import path

from core.views import index,contact,about,service,achievements

urlpatterns = [
    path('' , index, name='index'),
    path('contact/',contact , name= 'contact'),
    path('about/',about , name= 'about'),
    path('service/',service , name= 'service'),
    path('achievements/',achievements , name= 'achievements'),
    path('admin/', admin.site.urls),
]
