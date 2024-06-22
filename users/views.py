from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView, ListView
from . import models, forms


class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = 'users/registration.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        age = form.cleaned_data['age']
        if age < 5:
            self.object.group = 'Дети'
        elif age >= 5 and age <= 10:
            self.object.group = 'Дети'
        elif age >= 11 and age <= 18:
            self.object.group = 'Подростки'
        elif age >= 18 and age <= 50:
            self.object.group = 'Взрослые'
        else:
            self.object.group = 'Нет возрастной группы'
        self.object.save()
        return response


class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("users:user_list")


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    model = models.CustomUser

    def get_queryset(self):
        return models.CustomUser.objects.filter().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = getattr(self.request, 'group', 'Нет возрастной группы')
        return context
