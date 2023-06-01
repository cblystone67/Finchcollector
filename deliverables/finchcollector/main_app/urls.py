from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('all_finches/', views.all_finches_index, name='index'),
    path('all_finches/<int:finch_id>/', views.all_finches_details, name='details'),
    path('all_finches/create/', views.FinchCreate.as_view(), name="finch_create"),
    path('all_finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finch_update'),
    path('all_finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
    
    
]
