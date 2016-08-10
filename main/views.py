from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegistrationForm
from .models import Log


# @login_required
# @csrf_exempt
# def my_view(request):
#     if request.method == 'POST':
#         Log.objects.create(logger_name=request.POST['name'],
#                            level=request.POST['levelname'],
#                            message=request.POST['message'],
#                            sender=request.user)
#         #print(request.POST['message'])
#         #print(request.POST['levelname'])
#         #print(request.user)
#         #print(request.POST['name'])
#         return render(request, 'index.html')
#     else:
#         logger = Log.objects.all()
#         print(logger)
#         return render(request, 'index.html', context={'logger':logger})


@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class MainView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        Log.objects.create(logger_name=request.POST['name'],
                           level=request.POST['levelname'],
                           message=request.POST['message'],
                           sender=request.user)
        return render(request, 'index.html')

    def get(self, request, *args, **kwargs):
        logger = Log.objects.all()
        return render(request, 'index.html', context={'logger': logger})


#
# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid() and form.get_user():
#             login(request, form.get_user())
#             return HttpResponseRedirect('/')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', context={'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class LoginHandlerView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponse('OK')

    def post(self, request, *args, **kwargs):
        return super(LoginHandlerView, self).post(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect('/')



class LogoutView(View, LoginRequiredMixin):
    redirect_field_name = '/login/'
    def get(self, request):
        logout(self.request)
        return HttpResponseRedirect('/')


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect('/')