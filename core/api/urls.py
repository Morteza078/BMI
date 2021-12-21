from django.urls import path, include

urlpatterns = [
    path('account/', include('account.api.urls')),
    path('health/', include('health.api.urls')),
]
