# from django.http import HttpResponse
#
# def hello(request):
#     return HttpResponse("Hello world ! ")


from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hell World!'
    context['way']   =  'china good!'
    return render(request, 'html.html', context)
