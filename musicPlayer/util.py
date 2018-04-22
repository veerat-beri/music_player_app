# ALL REQUIRED LIBRARIES

# Django VIEWS related
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DeleteView, RedirectView
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse

# Django AUTH related
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as authViews, update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib import messages

# Django EXCEPTIONS related
from django.core.exceptions import ValidationError
from django.db import IntegrityError

#Django OTHERS
from django.conf.urls.static import static
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.conf import settings

# General
from pdb import set_trace as breakPoint
import os, logging



# GLOBAL CONFIGURATION

# LOGGER configuration
logging.basicConfig(
    format='%(name)-15s: %(levelname)-5s : %(message)s',
    level='INFO'
)
logger = logging.getLogger('music_player')
