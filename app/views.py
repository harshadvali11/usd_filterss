from django.shortcuts import render

# Create your views here.


def filters(request):
    import datetime
    dt=datetime.datetime.now()

    d={'data':'granny is wife of DocTOr ','dt':dt,'c':1}
    return render(request,'filters.html',d)




def myfilters(request):
    d={'data':'HAi HellO HoW ARE U'}
    return render(request,'myfilters.html',d)