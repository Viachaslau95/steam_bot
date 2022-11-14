from django.urls import path

from apps.items.views import GiveMoney

urlpatterns = [
    path('home/', GiveMoney.as_view())
]
