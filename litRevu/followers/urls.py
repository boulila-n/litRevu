from django.urls import path

from . import views

urlpatterns = [
    path('manage/', views.SubscribeCreateView.as_view(),
         name='manage_subscribe'),
    path('delete/<int:pk>', views.SubscribeDeleteView.as_view(),
         name='confirm_delete_followers'),

]
