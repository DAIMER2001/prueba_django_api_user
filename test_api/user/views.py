from unicodedata import category
from .models import User

from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json

from .models import User
# Create your views here.

class UserView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            users = list(User.objects.filter(id=id).values())
            if len(users) > 0:
                company = users[0]
                datos = {'message': "Success", 'company': company}
            else:
                datos = {'message': "Company not found"}
        else:
            users = list(User.objects.select_related('users__categories').values())
            if len(users)>0:
                datos = {'data': users}
            else:
                datos = {'message': "users not found"}
            return JsonResponse(datos)
    
    
    def post(self, request):
        request = json.loads(request.body)
        User.objects.create(icon_url= request['icon_url'], created_at= request['created_at'],updated_at= request['updated_at'],url= request['url'],value= request['value'])
        data = {'message': 'success'}
        return JsonResponse(data)
    
    
    