from django.db import models
from musicPlayer.util import *

class PlayList(models.Model):
    appUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlist')
    title = models.CharField(max_length=200, help_text='Enter a name for your playlist')
    objects = models.Manager()

    def clean(self):
        self.title = self.title.casefold()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.clean()
        return super(PlayList, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('appUser', 'title',)

class Track(models.Model):
    title = models.CharField(max_length=300, unique=True)
    artist = models.CharField(max_length=300, null=True, blank=True)
    playList = models.ForeignKey(PlayList, on_delete=models.SET_NULL, related_name='track', blank=True, null=True)
    songFile = models.FileField(upload_to='songsCollection/', unique=True)
    objects = models.Manager()

    def clean(self):
        file = self.songFile._file
        if file._size > 20 * 1024 * 1024:
            raise ValidationError("Audio file too large ( > 20mb )")

        if not file.content_type == 'audio/mp3':
            raise ValidationError(
                "Sorry, we do not support that type. Please try uploading an mp3 file, or other common audio type.")

    def __str__(self):
        return self.title
