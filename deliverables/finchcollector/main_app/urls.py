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
    path('all_finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_list'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('finch/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('finch/<int:finch_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
]
