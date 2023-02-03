from django.urls import path

from rest_framework.routers import DefaultRouter as DR
from mainapp.views import (
    UserView, SmsUserView, RegistrationView, AuthorizationView
)
router = DR()
router.register('users', UserView, basename='user')
router.register('smsusers', SmsUserView, basename='smsuser')

urlpatterns = [
    path('reg/', RegistrationView.as_view()),
    path('aut/', AuthorizationView.as_view())   
]
urlpatterns += router.urls
