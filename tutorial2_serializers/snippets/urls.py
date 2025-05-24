from django.urls import path
from .views import snippet_detail, snippet_list

urlpatterns = [
    path('snippets/', snippet_list),
    path('snippet/<int:pk>/', snippet_detail)
]