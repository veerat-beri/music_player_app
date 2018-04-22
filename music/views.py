from .models import *

class UserHome(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, *args, **kwargs):
        logger.info('_______WELCOME USER-{}________'.format(request.user.id))
        if request.user.is_superuser:
            return redirect('/admin/')
        userPlaylists = PlayList.objects.filter(appUser=request.user.id)
        return render(request, 'music/user_home_page.html', {'playLists': userPlaylists, 'noOfSongs': len(userPlaylists)})

class PlaylistManager(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, *args, **kwargs):
        songsOfPlaylist = PlayList.objects.get(id=kwargs['playListNo']).track.iterator()
        return render(request, 'music/playlist_songs_page.html', {'playlistSongs': songsOfPlaylist, 'playlistId': kwargs['playListNo']})

class PlaylistDelete(DeleteView):
    model = PlayList
    success_url = reverse_lazy('userHomePage')

class NewPlaylist(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, *args, **kwargs):
        logger.info('__________RENDERING NEW PLAYLIST PAGE_________')
        return render(request, 'music/new_playlist.html', {'songs': Track.objects.all(), 'error': None})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, *args, **kwargs):
        try:
            newPlaylist = PlayList(appUser=User.objects.get(id=request.user.id), title=request.POST['playlistName'])
            newPlaylist.save()
            for songId in request.POST.getlist('selectedSongsIdList[]'):
                newPlaylist.track.add(Track.objects.get(id=songId))
            return redirect('playListView', newPlaylist.id)
        except IntegrityError:
            return render(request, 'music/new_playlist.html', {'songs': Track.objects.all(), 'error': 'Playlist with this name already exist!!'})