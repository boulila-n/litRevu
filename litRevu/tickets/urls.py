from django.urls import path

from . import views

urlpatterns = [
    path('add', views.TicketCreateView.as_view(), name='add_ticket'),
    path('liste', views.PostsListView.as_view(), name='liste'),
    path('delete/<int:pk>', views.TicketDeleteView.as_view(),
         name='delete_ticket'),
    path('update/<int:pk>', views.TicketUpdateView.as_view(),
         name='update_ticket'),
    path('review_with_ticket/add/', views.ReviewWithTicket.as_view(),
         name='add_review_with_ticket'),
    path('review_with_ticket/update/<int:pk>',
         views.ReviewWithTicket.as_view(),
         name='update_review_with_ticket'),
    path('review/delete/<int:pk>', views.ReviewDeleteView.as_view(),
         name='delete_review'),
    path('review_without_ticket/update/<int:pk>',
         views.ReviewWithoutTicket.as_view(),
         name='update_review_without_ticket'),
]
