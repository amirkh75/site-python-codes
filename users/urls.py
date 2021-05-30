
from django.urls import path
from users import views


app_name = 'users'
urlpatterns = [
    path("<int:user_id>/", views.users_detail, name="users_detail"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
