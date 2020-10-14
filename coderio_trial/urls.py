from django.contrib import admin
from django.urls import path, include

app_name = 'coderio_trial'

urlpatterns = [
    path('secure_admin/', admin.site.urls),
    path('api/', include('character.api.urls')),
]
