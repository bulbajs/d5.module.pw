from django.urls import path
from .views import CreateAccount

urlpatterns = [
    path('signup/', CreateAccount.as_view(), name='signup'),
]