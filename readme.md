# music-player

A [django](https://www.djangoproject.com/) app for making playlists and to listen mp3 songs.

### Introduction

Its a simple app where users can listen to their songs by first signing up with their username and password; and then create playlists by choosing from available songs on the app.
Users can change password after logging in, and can also delete playlists.

Also, admin is responsible for uploading songs with title and artist name.

> These instructions are Ubuntu specific and for development server only.

### Installation

* Install [Python3](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)
* make virtualenv and activate it:
    ```
    sudo pip install virtualenv
    virtualenv -p python3 \*venvName\*
    . venvName/bin/activate
    ```
* Clone Repository

### Setup

* Move into base app directory and install required packages by running:
    ```
    pip install -r requirements.txt
    ```
* Make dB and migrations:
    ```
    ./manage.py makemigrations music
    ./manage.py migrate
    ``` 
* Create superuser, so that you can upload songs from app online.
* You are good to go, boot up the server:
    ```
    ./manage.py runserver
    ```
* Go to browser and use app by entering url:
    ```
    localhost:8000
    ```
* To stop the development server, go to cmd and press "Ctrl+c".
