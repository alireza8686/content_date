from django.urls import path
from .views import panel_view

urlpatterns = [
    path('<int:user_id>/', panel_view, name='panel'),
]
