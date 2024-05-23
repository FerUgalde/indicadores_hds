from django.urls import path
from .views.index import HomePageView
from .views.login import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    # Login
    path('login/', CustomLoginView.as_view(), name='login'),

    # Logout
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
