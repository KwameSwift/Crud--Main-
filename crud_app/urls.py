from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, userProfileDetailView, userView, LoginView

# router=DefaultRouter()

# router.register("all-profiles",UserProfileListCreateView)
# router.register("profile/<int:pk>",userProfileDetailView,basename='profile')

urlpatterns = [
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
    path("profile", UserProfileListCreateView.as_view(), name="profile_view"),
    path("login", LoginView.as_view(), name="login"),
    path("users", userView.as_view(), name="user_view")
    # path("",include(router.urls))
]
