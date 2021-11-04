from django.shortcuts import render
from account.models import User
from openapp.models import Open_1, Open_2, Open_3, Open_4, Open_5, Open_6, Open_7, Open_8, Open_9
# Create your views here.

def home(request):
    # user_id = request.session.get('user')
    # if user_id:
    #     user = User.objects.get(pk = user_id)
    #     return render(request, 'home.html', {'user': user})

    open_index_1 = Open_1.objects.all()
    list_open = []
    for open in open_index_1:
        list_open.append(open)

    list_like = []
    for open in open_index_1:
        list_like.append(open.like_count)

    num = len(list_open)

    if num == 0:
        return render(request, 'home.html')

    index = list_like.index(max(list_like))
    hot_open_11 = list_open[index]

    del list_open[index]
    del list_like[index]

    if num == 1:

        return render(request, 'home.html', {'hot_open_11' : hot_open_11})
    

    index = list_like.index(max(list_like))
    hot_open_12 = list_open[index]

    del list_open[index]
    del list_like[index]

    if num == 2:

        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12})


    index = list_like.index(max(list_like))
    hot_open_13 = list_open[index]

    del list_open[index]
    del list_like[index]


    if num == 3:

        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13})

    index = list_like.index(max(list_like))
    hot_open_14 = list_open[index]

    return render(request, 'home.html', {'hot_open_11' : hot_open_11, 
    'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14})

def search(request):
    query = request.GET['query']
    if query:
        open1 = Open_1.objects.filter(title__contains=query) 
        open2 = Open_2.objects.filter(title__contains=query)
        open3 = Open_3.objects.filter(title__contains=query)
        open4 = Open_4.objects.filter(title__contains=query)
        open5 = Open_5.objects.filter(title__contains=query)
        open6 = Open_6.objects.filter(title__contains=query)
        open7 = Open_7.objects.filter(title__contains=query)
        open8 = Open_8.objects.filter(title__contains=query)
        open9 = Open_9.objects.filter(title__contains=query)      
    return render(request, 'search.html', { 'open1': open1, 'open2': open2, 'open3': open3, 'open4': open4, 'open5': open5, 'open6': open6, 'open7': open7,
    'open8': open8, 'open9': open9 })

