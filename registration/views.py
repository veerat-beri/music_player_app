from musicPlayer.util import *

class SignUp(View):

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            rawPassword = form.cleaned_data.get('password1')
            user = authenticate(username=userName, password=rawPassword)
            login(request, user)
            return redirect('userHomePage')

        return render(request, 'registration/sign_up.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': form})

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
