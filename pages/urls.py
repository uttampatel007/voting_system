from django.urls import path

from .views import home, AboutPageView, cast_vote

app_name = "pages"

urlpatterns = [
    path("", home, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("vote/<str:vote_for>/", cast_vote, name="vote"),
]
