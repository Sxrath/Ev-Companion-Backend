from django.urls import path

from .views import  CreateFeedback,ListallChargingStations, ListChargingStations,BookReservation, ListFeedback,ListRservation,DeleteReservation, LoginView, Register


urlpatterns=[
    path('register/',Register.as_view(),name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('list-stations/<int:location_id>/',ListChargingStations.as_view(), name='list-stations'),
    path('create-Reservation/<int:spot_id>/',BookReservation.as_view(),name='book-reservation'),
    path('List-reservation/',ListRservation.as_view(),name='lis-reservations'),
    path('Delete-reservation/<int:pk>/',DeleteReservation.as_view(),name='dlt-reservation'),
    path('add-feedback/<int:spot_id>/',CreateFeedback.as_view(),name='fdbck'),
    path('list-feedbak/<int:spot_id>/',ListFeedback.as_view(),name='lis-fdbck'),
    path('listallstation/',ListallChargingStations.as_view(),name='all')
]