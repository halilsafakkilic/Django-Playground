from django.urls import path

from . import views
from .controllers import api_questions

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/<int:id>/', api_questions.detail, name='detail.api'),
    path('api/add', api_questions.add, name='add.api'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
