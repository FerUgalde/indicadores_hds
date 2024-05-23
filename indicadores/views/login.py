from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        print('login')
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'error': 'Invalid credentials'})


class CustomLogoutView(LoginView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        print('logout')
        logout(request)
        return redirect('login')
