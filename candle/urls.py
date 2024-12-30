from django.urls import path
from .views import HomeView,CandleLoginView

app_name = "candle"

urlpatterns = [
    path("login/",CandleLoginView.as_view(),name="login"),
    path("",HomeView.as_view(),name="home"),
]

