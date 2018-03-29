from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def add_quiz(request):
    return render(request, 'addquiz.html')

def success(request):
    return render(request, 'success.html', {'quiz': request.POST['quiz'], 'ans': request.POST['ans']})
