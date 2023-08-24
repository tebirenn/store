from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect('market:home')

    return render(request, 'authe/signup.html')