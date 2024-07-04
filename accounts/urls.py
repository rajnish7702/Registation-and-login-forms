from django.urls import path
from .views import user_signup,login,protected_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', user_signup, name='signup'),
    path('login/', login, name='login'),
    path('protected/', protected_view, name='protected'),

]
