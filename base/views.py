from django.shortcuts import render

# Create your views here.
def home (request):
    context=dict()
    return render(request,'base/home.html',context)

def profile(request,name):
    name=name
    context=dict(name=name)
    return render(request,'base/profile.html',context)