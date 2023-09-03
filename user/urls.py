from django.urls import path
from . import views

urlpatterns = [
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("delete/<int:id>",views.delete_profile,name="delete_profile"),
    path('profile/<str:username>',views.profile,name="profile"),
    path('logout',views.logout_view,name="logout" ),
]

handler404 = 'user.views.custom_404'