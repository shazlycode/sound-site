"""sound URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django .conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('baset', views.basetview, name='baset'),
    path('radio', views.radioview, name='radio'),
    path('basetplay/<int:sound_id>', views.baset_play, name='basetplay'),
    path('radioplay/<int:radio_id>', views.radio_play, name='radioplay'),
    path('minshawy', views.minshview, name='minshawy'),
    path('minshawyplay/<int:sound_id>', views.minshawy_play, name='minshawyplay'),
    path('husary', views.husaryview, name='husary'),
    path('husaryplay/<int:sound_id>', views.husary_play, name='husaryplay'),
    
    
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
