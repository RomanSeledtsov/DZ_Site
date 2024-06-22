from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest
from django.core.exceptions import ValidationError


class AgeGroupMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            age = int(request.POST.get('age'))
            if age < 5:
                return HttpResponseBadRequest('Ты слишком маленький для регистрации')
            elif age >= 5 and age <= 10:
                request.group = 'Дети'
            elif age >= 11 and age <= 18:
                request.group = 'Подростки'
            elif age >= 18 and age <= 50:
                request.group = 'Взрослые'
            else:
                return HttpResponseBadRequest('Превышен допустимый возраст регистрации, помолодей')

        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'group', 'Нет возрастной группы')
