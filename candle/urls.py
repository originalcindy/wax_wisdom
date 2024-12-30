from django.urls import path
from .views import HomeView,CandleLoginView,CandleSignUpView

app_name = "candle"

urlpatterns = [
    path("login/",CandleLoginView.as_view(),name="login"),
    path('signup/', CandleSignUpView.as_view(), name='signup'),
    path("",HomeView.as_view(),name="home"),
]

