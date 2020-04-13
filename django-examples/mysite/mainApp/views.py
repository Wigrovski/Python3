from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/home.html')
def contact(request):
    return render(request, 'mainApp/basic.html',
                  {"values": ['Если возникли вопросы то звоните','+66 060 4035','example@mail.ru']})

