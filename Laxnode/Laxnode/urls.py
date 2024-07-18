
from django.contrib import admin
from django.urls import path

from core.views import index,contact,about,work,achievements

urlpatterns = [
    path('' , index, name='index'),
    path('contact/',contact , name= 'contact'),
    path('about/',about , name= 'about'),
    path('work/',work , name= 'work'),
    path('achievements/',achievements , name= 'achievements'),
    path('admin/', admin.site.urls),
]
