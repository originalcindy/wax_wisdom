from django.urls import path
from .views import DashboardView,DashboardBlogView,BlogDeleteView,DashboardWorkshopView,DashboardBookingView

urlpatterns = [
    path("bookings/",DashboardBookingView.as_view(),name="dashboard_bookings"),
    path("workshops/",DashboardWorkshopView.as_view(),name="dashboard_workshops"),
    path("blogs/<int:pk>/delete/",BlogDeleteView.as_view(),name="delete_blogs"),
    path("blogs/",DashboardBlogView.as_view(),name="dashboard_blogs"),
    path("",DashboardView.as_view(),name="dashboard")
]
