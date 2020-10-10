from django.urls import path
from Main import views

# Patterns for session related URLs
urlpatterns = [
    path('<int:id>', views.session_detail, name="SessionDetail"),
    path('new', views.new, name="new")
]
