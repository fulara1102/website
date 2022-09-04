from unicodedata import name
from . import views
from django.urls import path

app_name = 'foods'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:item_id>/',views.detail,name='detail'),
    path('time/',views.time,name='time'),
    path('report/',views.report,name='report'),
    path('history/',views.history,name='history'),

    #add items
    path('add',views.create_item,name='create_item'),
    #edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    
]