from django.urls import path
from .views import WorkerView

urlpatterns = [
    path('worker/', WorkerView.as_view()),
]
