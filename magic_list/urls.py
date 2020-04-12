from django.urls import path
from . import views
urlpatterns=[path("",views.home,name='home'),path('searchresult/',views.new_search,name='new_search')]