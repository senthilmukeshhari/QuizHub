from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('questions',views.questions,name='questions'),
    path('result',views.result,name='result'),
    path('feedback_result',views.FeedbackResult,name="fbr")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)