from django.urls import path
from shop import views 
from .views import SignUpView, ProfileCreateView, ProfileUpDateView, ProfileDetailView

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
    path("create_profile/",  ProfileCreateView.as_view(), name="create_profile"),
    path("update_profile/<int:pk>/", ProfileUpDateView.as_view(), name="update_profile"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile"),

]
