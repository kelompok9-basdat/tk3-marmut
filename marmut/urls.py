"""
URL configuration for marmut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('royalti/', include('royalti.urls')),
    path('label/', include('album_song.urls')),
    path('kelola/', include('kelola_alsong.urls')),
    path('', include('authentication.urls')),
    path('downloaded/', include('downloaded_songs.urls')),
    path('search/', include('downloaded_songs.urls')),
    path('manage_playlist', include('kelola_playlist.urls')),
    path('play_song', include('play_song.urls')),
    path('play_user_playlist', include('play_user_playlist.urls')),
    path('langganan/', include('langganan.urls')),
    path('riwayat/', include('langganan.urls')),
    path('kelola_podcast/', include('kelola_podcast.urls')),
]
