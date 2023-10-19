from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import AnswerModelViewSet, QuestionModelViewSet, SubmitAPIView


router = DefaultRouter()
router.register(r"questions", QuestionModelViewSet)
router.register(r"answers", AnswerModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/submit/", SubmitAPIView.as_view()),
    path("web/", include("web.urls")),
]
