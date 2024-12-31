from django.urls import path
from .views import (
    HomeView,CandleLoginView,CandleSignUpView,CandleLogoutView,
    AboutView,BlogListView,WorkshopListView,BlogDetail,
    BookingCreateView
)

app_name = "candle"

urlpatterns = [
    path('bookings/',BookingCreateView.as_view(), name='bookings'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path("workshops/",WorkshopListView.as_view(),name="workshops"),
    path("blogs/",BlogListView.as_view(),name="blogs"),
    path("about-us/",AboutView.as_view(),name="aboutus"),
    path('logout/', CandleLogoutView.as_view(), name='logout'),
    path("login/",CandleLoginView.as_view(),name="login"),
    path('signup/', CandleSignUpView.as_view(), name='signup'),
    path("",HomeView.as_view(),name="home"),
]

