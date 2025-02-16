from django.urls import path,include
from .views import (
    HomeView,CandleLoginView,CandleSignUpView,CandleLogoutView,
    AboutView,BlogListView,WorkshopListView,BlogDetail,
    BookingCreateView,BookingDeleteView,BookingUpdateView,ReviewCreateView
)

app_name = "candle"

urlpatterns = [
    path("dashboard/",include("candle.dashboard_urls")),
    path("rate/",ReviewCreateView.as_view(),name="rate_workshop"),
    path("bookings/update/",BookingUpdateView.as_view(),name="update_bookings"),
    path("bookings/<int:pk>/delete/",BookingDeleteView.as_view(),name="delete_bookings"),
    path('bookings/create/',BookingCreateView.as_view(), name='create_bookings'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path("workshops/",WorkshopListView.as_view(),name="workshops"),
    path("blogs/",BlogListView.as_view(),name="blogs"),
    path("about-us/",AboutView.as_view(),name="aboutus"),
    path('logout/', CandleLogoutView.as_view(), name='logout'),
    path("login/",CandleLoginView.as_view(),name="login"),
    path('signup/', CandleSignUpView.as_view(), name='signup'),
    path("",HomeView.as_view(),name="home"),
]

