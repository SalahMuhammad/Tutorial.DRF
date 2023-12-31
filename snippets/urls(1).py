from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.SnippetList.as_view(), name='snippet-list'),
    path('<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]

# support adding suffix, like .html .json etc
urlpatterns = format_suffix_patterns(urlpatterns)
