from django.contrib import admin
from django.urls import path, re_path
from registration.views import *
from music.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='appAdmin'),
    path('', TemplateView.as_view(template_name='registration/base.html'), name="home"),
    path('login/', authViews.login, name='login'),
    path('logout/', authViews.logout, {'next_page': '/'}, name='logout'),
    path('signup/', SignUp.as_view(), name='signUp'),
    re_path(r'^password_reset/$', changePassword, name='change_password'),
    re_path(r'^delete/(?P<pk>\d+)/$', PlaylistDelete.as_view(), name="deletePlaylist"),
    path('home/', UserHome.as_view(), name='userHomePage'),
    path('accounts/profile/', RedirectView.as_view(pattern_name='userHomePage', permanent=True)),
    re_path(r'^NewPlaylist/$', NewPlaylist.as_view(), name='createNewPlaylist'),
    re_path(r'^playList/(?P<playListNo>[0-9]+)/$', PlaylistManager.as_view(), name='playListView'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
