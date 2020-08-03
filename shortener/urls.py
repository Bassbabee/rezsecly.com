from django.urls import path, re_path

from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.HomeView.as_view()),
    re_path(r'(?P<shortcode>[\w-]+)/$', views.RezRedirectCBView.as_view(), name="shortcode"),
]
