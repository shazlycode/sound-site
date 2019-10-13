from django.shortcuts import render, get_object_or_404
from .models import Baset, Radio, Menshawy
# Create your views here.

def index(request):
    
    context= {
        'title':'الرئيسية',
    }
    return render(request, 'app/index.html',context)

def basetview(request):
    sounds= Baset.objects.all()
    context={
        'title':'عبد الباسط عبد الصمد',
        'sounds':sounds,
        
    }
    return render(request, 'app/baset.html', context)

def radioview(request):
    radios= Radio.objects.all()
    context={
        'title':'الراديو',
        'radios':radios,
    }
    return render(request, 'app/radio.html', context)


def baset_play(request, sound_id):
    track=get_object_or_404(Baset, pk=sound_id)
    
    
    context={
        'title':'تشغيل عبد الباسط',
        'track':track,
        
    }
    return render(request, 'app/basetplay.html', context)

def radio_play(request, radio_id):
    radiotrack= get_object_or_404(Radio, pk=radio_id)
    context={
        'title':'تشغيل الراديو',
        'radiotrack':radiotrack,
    }
    return render(request, 'app/radioplay.html', context)