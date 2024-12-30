from django.urls import path
from .views import HomeView,CandleLoginView,CandleSignUpView,CandleLogoutView,AboutView

app_name = "candle"

urlpatterns = [
    path("about-us/",AboutView.as_view(),name="aboutus"),
    path('logout/', CandleLogoutView.as_view(), name='logout'),
    path("login/",CandleLoginView.as_view(),name="login"),
    path('signup/', CandleSignUpView.as_view(), name='signup'),
    path("",HomeView.as_view(),name="home"),
]

