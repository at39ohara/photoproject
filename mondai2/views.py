from django.shortcuts import render

def TopView(request):
    print(request)
    print(render(request, 'top.html'))
    return render(request, 'top.html')
