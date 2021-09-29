from django.shortcuts import render
from account.models import User
# Create your views here.

def home(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        return render(request, 'home.html', {'user': user})
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')