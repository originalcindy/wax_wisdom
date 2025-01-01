from django.urls import path
from .views import DashboardView,DashboardBlogView,BlogDeleteView

urlpatterns = [
    path("blogs/<int:pk>/delete/",BlogDeleteView.as_view(),name="delete_blogs"),
    path("blogs/",DashboardBlogView.as_view(),name="dashboard_blogs"),
    path("",DashboardView.as_view(),name="dashboard")
]
