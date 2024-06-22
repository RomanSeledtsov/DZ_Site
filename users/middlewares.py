from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest
from django.core.exceptions import ValidationError


# class AgeGroupMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         if request.path == '/register/' and request.method == 'POST':
#             age = int(request.POST.get('age'))
#             if age < 5:
#                 return HttpResponseBadRequest('Ты слишком маленький для регистрации')
#             elif age >= 5 and age <= 10:
#                 request.group = 'Дети'
#             elif age >= 11 and age <= 18:
#                 request.group = 'Подростки'
#             elif age >= 18 and age <= 50:
#                 request.group = 'Взрослые'
#             else:
#                 return HttpResponseBadRequest('Превышен допустимый возраст регистрации, помолодей')
#
#         elif request.path == '/register/' and request.method == 'GET':
#             setattr(request, 'group', 'Нет возрастной группы')

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class AgeGroupMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            age = int(request.POST.get("age"))
            if age < 5:
                return HttpResponseBadRequest("Возраст не подходит для регистрации (слишком малы)")
            elif age >= 5 and age <= 10:
                request.group = "Детский"
            elif age >= 11 and age <= 18:
                request.group = "Подростковый"
            elif age >= 18 and age <= 45:
                request.group = "Взрослый"
            else:
                return HttpResponseBadRequest("Возраст не подходит дл регистрации (ты старый)")
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "group", "Нет возрастной группы")