from django.shortcuts import render, redirect
from account.models import User
from django.contrib import auth
from moin_1.models import Open_1
from moin_2.models import Open_2
from moin_3.models import Open_3
from moin_4.models import Open_4
from moin_5.models import Open_5
from moin_6.models import Open_6
from moin_7.models import Open_7
from moin_8.models import Open_8
from moin_9.models import Open_9

def select(request):
    return render(request, 'select.html')

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
        return render(request, 'search.html', { 'open1': open1, 'open2': open2, 'open3': open3, 'open4': open4, 'open5': open5, 'open6': open6, open7: 'open7', open8: 'open8', 'open9': open9, 'query':query })
    else:
        return render(request,'searchNone.html')

def mypage(request):
    open_1 = Open_1.objects.all()
    open_2 = Open_2.objects.all()
    open_3 = Open_3.objects.all()
    open_4 = Open_4.objects.all()
    open_5 = Open_5.objects.all()
    open_6 = Open_6.objects.all()
    open_7 = Open_7.objects.all()
    open_8 = Open_8.objects.all()
    open_9 = Open_9.objects.all()
    return render(request, 'mypage.html', {'open_1': open_1, 'open_2': open_2, 'open_3': open_3, 'open_4': open_4, 'open_5': open_5, 'open_6': open_6, 'open_7': open_7, 'open_8': open_8, 'open_9': open_9})

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    open_index_1 = Open_1.objects.all()
    list_open_1 = []
    for open in open_index_1:
        list_open_1.append(open)

    list_like_1 = []
    for open in open_index_1:
        list_like_1.append(open.like_count)
    
    num_1 = len(list_open_1)
    
    if num_1 == 0:
        return render(request, 'home.html')
    index_1 = list_like_1.index(max(list_like_1))
    hot_open_11 = list_open_1[index_1]

    del list_open_1[index_1]
    del list_like_1[index_1]

    if num_1 == 1:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11})

    index_1 = list_like_1.index(max(list_like_1))
    hot_open_12 = list_open_1[index_1]

    del list_open_1[index_1]
    del list_like_1[index_1]

    if num_1 == 2:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12})
    index_1 = list_like_1.index(max(list_like_1))
    hot_open_13 = list_open_1[index_1]

    del list_open_1[index_1]
    del list_like_1[index_1]

    if num_1 == 3:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13})

    index_1 = list_like_1.index(max(list_like_1))
    hot_open_14 = list_open_1[index_1]

    del list_open_1[index_1]
    del list_like_1[index_1]

    if num_1 == 4:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14})

    index_1 = list_like_1.index(max(list_like_1))
    hot_open_15 = list_open_1[index_1]
    
    open_index_2 = Open_2.objects.all()
    list_open_2 = []
    for open in open_index_2:
        list_open_2.append(open)

    list_like_2 = []
    for open in open_index_2:
        list_like_2.append(open.like_count)

    num_2 = len(list_open_2)

    if num_2 == 0:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15})

    index_2 = list_like_2.index(max(list_like_2))
    hot_open_21 = list_open_2[index_2]

    del list_open_2[index_2]
    del list_like_2[index_2]

    if num_2 == 1:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21})

    index_2 = list_like_2.index(max(list_like_2))
    hot_open_22 = list_open_2[index_2]

    del list_open_2[index_2]
    del list_like_2[index_2]

    if num_2 == 2:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22})
    index_2 = list_like_2.index(max(list_like_2))
    hot_open_23 = list_open_2[index_2]

    del list_open_2[index_2]
    del list_like_2[index_2]

    if  num_2 == 3:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23})

    index_2 = list_like_2.index(max(list_like_2))
    hot_open_24 = list_open_2[index_2]

    del list_open_2[index_2]
    del list_like_2[index_2]

    if num_2 == 4:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24})

    index_2 = list_like_2.index(max(list_like_2))
    hot_open_25 = list_open_2[index_2]

    open_index_3 = Open_3.objects.all()
    list_open_3 = []
    for open in open_index_3:
        list_open_3.append(open)

    list_like_3 = []
    for open in open_index_3:
        list_like_3.append(open.like_count)

    num_3 = len(list_open_3)

    if num_3 == 0:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,})

    index_3 = list_like_3.index(max(list_like_3))
    hot_open_31 = list_open_3[index_3]

    del list_open_3[index_3]
    del list_like_3[index_3]

    if num_3 == 1:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31': hot_open_31})

    index_3 = list_like_3.index(max(list_like_3))
    hot_open_32 = list_open_3[index_3]

    del list_open_3[index_3]
    del list_like_3[index_3]

    if num_3 == 2:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32})

    index_3 = list_like_3.index(max(list_like_3))
    hot_open_33 = list_open_3[index_3]

    del list_open_3[index_3]
    del list_like_3[index_3]

    if num_3 == 3:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33})

    index_3 = list_like_3.index(max(list_like_3))
    hot_open_34 = list_open_3[index_3]

    del list_open_3[index_3]
    del list_like_3[index_3]

    if num_3 == 4:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34})

    index_3 = list_like_3.index(max(list_like_3))
    hot_open_35 = list_open_3[index_3]

    open_index_4 = Open_4.objects.all()
    list_open_4 = []
    for open in open_index_4:
        list_open_4.append(open)

    list_like_4 = []
    for open in open_index_4:
        list_like_4.append(open.like_count)

    num_4 = len(list_open_4)

    if num_4 == 0:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35})

    index_4 = list_like_4.index(max(list_like_4))
    hot_open_41 = list_open_4[index_4]

    del list_open_4[index_4]
    del list_like_4[index_4]

    if num_4 == 1:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41})

    index_4 = list_like_4.index(max(list_like_4))
    hot_open_42 = list_open_4[index_4]

    del list_open_4[index_4]
    del list_like_4[index_4]

    if num_4 == 2:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42})

    index_4 = list_like_4.index(max(list_like_4))
    hot_open_43 = list_open_4[index_4]

    del list_open_4[index_4]
    del list_like_4[index_4]

    if num_4 == 3:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43})

    index_4 = list_like_4.index(max(list_like_4))
    hot_open_44 = list_open_4[index_4]

    del list_open_4[index_4]
    del list_like_4[index_4]

    if num_4 == 4:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34,'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44})

    index_4 = list_like_4.index(max(list_like_4))
    hot_open_45 = list_open_4[index_4]

    open_index_5 = Open_5.objects.all()
    list_open_5 = []
    for open in open_index_5:
        list_open_5.append(open)

    list_like_5 = []
    for open in open_index_5:
        list_like_5.append(open.like_count)

    num_5 = len(list_open_5)

    if num_5 == 0:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45})

    index_5 = list_like_5.index(max(list_like_5))
    hot_open_51 = list_open_5[index_5]

    del list_open_5[index_5]
    del list_like_5[index_5]

    if num_5 == 1:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51})

    index_5 = list_like_5.index(max(list_like_5))
    hot_open_52 = list_open_5[index_5]

    del list_open_5[index_5]
    del list_like_5[index_5]

    if num_5 == 2:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52})

    index_5 = list_like_5.index(max(list_like_5))
    hot_open_53 = list_open_5[index_5]

    del list_open_5[index_5]
    del list_like_5[index_5]

    if num_5 == 3:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53})

    index_5 = list_like_5.index(max(list_like_5))
    hot_open_54 = list_open_5[index_5]

    del list_open_5[index_5]
    del list_like_5[index_5]

    if num_5 == 4:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34,'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54})

    index_5 = list_like_5.index(max(list_like_5))
    hot_open_55 = list_open_5[index_5]

    open_index_6 = Open_6.objects.all()
    list_open_6 = []
    for open in open_index_6:
        list_open_6.append(open)

    list_like_6 = []
    for open in open_index_6:
        list_like_6.append(open.like_count)

    num_6 = len(list_open_6)

    if num_6 == 0:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55})

    index_6 = list_like_6.index(max(list_like_6))
    hot_open_61 = list_open_6[index_6]

    del list_open_6[index_6]
    del list_like_6[index_6]

    if num_6 == 1:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61})

    index_6 = list_like_6.index(max(list_like_6))
    hot_open_62 = list_open_6[index_6]

    del list_open_6[index_6]
    del list_like_6[index_6]

    if num_6 == 2:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62})

    index_6 = list_like_6.index(max(list_like_6))
    hot_open_63 = list_open_6[index_6]

    del list_open_6[index_6]
    del list_like_6[index_6]

    if num_6 == 3:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63})

    index_6 = list_like_6.index(max(list_like_6))
    hot_open_64 = list_open_6[index_6]

    del list_open_6[index_6]
    del list_like_6[index_6]

    if num_6 == 4:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34,'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64,})

    index_6 = list_like_6.index(max(list_like_6))
    hot_open_65 = list_open_6[index_6]

    open_index_7 = Open_7.objects.all()
    list_open_7 = []
    for open in open_index_7:
        list_open_7.append(open)

    list_like_7 = []
    for open in open_index_7:
        list_like_7.append(open.like_count)

    num_7 = len(list_open_7)

    if num_7 == 0:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65})

    index_7 = list_like_7.index(max(list_like_7))
    hot_open_71 = list_open_7[index_7]

    del list_open_7[index_7]
    del list_like_7[index_7]

    if num_7 == 1:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71})

    index_7 = list_like_7.index(max(list_like_7))
    hot_open_72 = list_open_7[index_7]

    del list_open_7[index_7]
    del list_like_7[index_7]

    if num_7 == 2:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72})

    index_7 = list_like_7.index(max(list_like_7))
    hot_open_73 = list_open_7[index_7]

    del list_open_7[index_7]
    del list_like_7[index_7]

    if num_7 == 3:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73})

    index_7 = list_like_7.index(max(list_like_7))
    hot_open_74 = list_open_7[index_7]

    del list_open_7[index_7]
    del list_like_7[index_7]

    if num_7 == 4:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34,'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74})

    index_7 = list_like_7.index(max(list_like_7))
    hot_open_75 = list_open_7[index_7]

    open_index_8 = Open_8.objects.all()
    list_open_8 = []
    for open in open_index_8:
        list_open_8.append(open)

    list_like_8 = []
    for open in open_index_8:
        list_like_8.append(open.like_count)

    num_8 = len(list_open_8)

    if num_8 == 0:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75})

    index_8 = list_like_8.index(max(list_like_8))
    hot_open_81 = list_open_8[index_8]

    del list_open_8[index_8]
    del list_like_8[index_8]

    if num_8 == 1:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
        'hot_open_81' : hot_open_81,})

    index_8 = list_like_8.index(max(list_like_8))
    hot_open_82 = list_open_8[index_8]

    del list_open_8[index_8]
    del list_like_8[index_8]

    if num_8 == 2:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
        'hot_open_81' : hot_open_81, 'hot_open_82' : hot_open_82})

    index_8 = list_like_8.index(max(list_like_8))
    hot_open_83 = list_open_8[index_8]

    del list_open_8[index_8]
    del list_like_8[index_8]

    if num_8 == 3:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
        'hot_open_81' : hot_open_81, 'hot_open_82' : hot_open_82, 'hot_open_83' : hot_open_83})

    index_8 = list_like_8.index(max(list_like_8))
    hot_open_84 = list_open_8[index_8]

    del list_open_8[index_8]
    del list_like_8[index_8]

    if num_8 == 4:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34,'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
        'hot_open_81' : hot_open_81, 'hot_open_82' : hot_open_82, 'hot_open_83' : hot_open_83, 'hot_open_84' : hot_open_84})

    index_8 = list_like_8.index(max(list_like_8))
    hot_open_85 = list_open_8[index_8]

    open_index_9 = Open_9.objects.all()
    list_open_9 = []
    for open in open_index_9:
        list_open_9.append(open)

    list_like_9 = []
    for open in open_index_9:
        list_like_9.append(open.like_count)

    num_9 = len(list_open_9)

    if num_9 == 0:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
        'hot_open_81' : hot_open_81, 'hot_open_82' : hot_open_82, 'hot_open_83' : hot_open_83, 'hot_open_84' : hot_open_84, 'hot_open_85' : hot_open_85})

    index_9 = list_like_9.index(max(list_like_9))
    hot_open_91 = list_open_9[index_9]

    del list_open_9[index_9]
    del list_like_9[index_9]

    if num_9 == 1:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
        'hot_open_81' : hot_open_81, 'hot_open_82' : hot_open_82, 'hot_open_83' : hot_open_83, 'hot_open_84' : hot_open_84, 'hot_open_85' : hot_open_85,
        'hot_open_91' : hot_open_91,})

    index_9 = list_like_9.index(max(list_like_9))
    hot_open_92 = list_open_9[index_9]

    del list_open_9[index_9]
    del list_like_9[index_9]

    if num_9 == 2:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
        'hot_open_81' : hot_open_81, 'hot_open_82' : hot_open_82, 'hot_open_83' : hot_open_83, 'hot_open_84' : hot_open_84, 'hot_open_85' : hot_open_85,
        'hot_open_91' : hot_open_91, 'hot_open_92' : hot_open_92})

    index_9 = list_like_9.index(max(list_like_9))
    hot_open_93 = list_open_9[index_9]

    del list_open_9[index_9]
    del list_like_9[index_9]

    if num_9 == 3:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
        'hot_open_81' : hot_open_81, 'hot_open_82' : hot_open_82, 'hot_open_83' : hot_open_83, 'hot_open_84' : hot_open_84, 'hot_open_85' : hot_open_85,
        'hot_open_91' : hot_open_91, 'hot_open_92' : hot_open_92, 'hot_open_93' : hot_open_93})

    index_9 = list_like_9.index(max(list_like_9))
    hot_open_94 = list_open_9[index_9]

    del list_open_9[index_9]
    del list_like_9[index_9]

    if num_9 == 4:
        return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
        'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
        'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34,'hot_open_35' : hot_open_35,
        'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
        'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
        'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
        'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
        'hot_open_81' : hot_open_81, 'hot_open_82' : hot_open_82, 'hot_open_83' : hot_open_83, 'hot_open_84' : hot_open_84, 'hot_open_85' : hot_open_85,
        'hot_open_91' : hot_open_91, 'hot_open_92' : hot_open_92, 'hot_open_93' : hot_open_93, 'hot_open_94' : hot_open_94})

    index_9 = list_like_9.index(max(list_like_9))
    hot_open_95 = list_open_9[index_9]

    del list_open_9[index_9]
    del list_like_9[index_9]

    return render(request, 'home.html', {'hot_open_11' : hot_open_11, 'hot_open_12' : hot_open_12, 'hot_open_13' : hot_open_13, 'hot_open_14' : hot_open_14, 'hot_open_15' : hot_open_15,
    'hot_open_21' : hot_open_21, 'hot_open_22' : hot_open_22, 'hot_open_23' : hot_open_23, 'hot_open_24' : hot_open_24, 'hot_open_25' : hot_open_25,
    'hot_open_31' : hot_open_31, 'hot_open_32' : hot_open_32, 'hot_open_33' : hot_open_33, 'hot_open_34' : hot_open_34, 'hot_open_35' : hot_open_35,
    'hot_open_41' : hot_open_41, 'hot_open_42' : hot_open_42, 'hot_open_43' : hot_open_43, 'hot_open_44' : hot_open_44, 'hot_open_45' : hot_open_45,
    'hot_open_51' : hot_open_51, 'hot_open_52' : hot_open_52, 'hot_open_53' : hot_open_53, 'hot_open_54' : hot_open_54, 'hot_open_55' : hot_open_55,
    'hot_open_61' : hot_open_61, 'hot_open_62' : hot_open_62, 'hot_open_63' : hot_open_63, 'hot_open_64' : hot_open_64, 'hot_open_65' : hot_open_65,
    'hot_open_71' : hot_open_71, 'hot_open_72' : hot_open_72, 'hot_open_73' : hot_open_73, 'hot_open_74' : hot_open_74, 'hot_open_75' : hot_open_75,
    'hot_open_81' : hot_open_81, 'hot_open_82' : hot_open_82, 'hot_open_83' : hot_open_83, 'hot_open_84' : hot_open_84, 'hot_open_85' : hot_open_85,
    'hot_open_91' : hot_open_91, 'hot_open_92' : hot_open_92, 'hot_open_93' : hot_open_93, 'hot_open_94' : hot_open_94, 'hot_open_95' : hot_open_95,})