from django.urls import path
from .import views

urlpatterns = [
    path('',views.add_your_data,name='home'),
    path('delete_data/<int:id>/',views.delete_data,name='delete'),
    path('update_data/<int:id>/',views.update_data,name='update'),
    
]
