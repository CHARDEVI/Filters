from django.shortcuts import render

# Create your views here.

def built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'Mahendra Singh Dhoni commonly known as MS Dhoni','c':'2','dt':dt}
    return render(request,'built_in_filters.html',d)