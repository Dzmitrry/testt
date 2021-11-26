from django.urls import path
from main import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("feedbacks", views.FeedbackViewSet)


urlpatterns = [
    path('', views.index),
    path("feedback-list/", views.feedback_list, name="feedback-list"),
] + router.urls
