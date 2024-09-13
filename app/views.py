from django.shortcuts import render # type: ignore

# Create your views here.
def one(request):
    return render(request,'one.html')