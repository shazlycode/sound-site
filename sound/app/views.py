from django.shortcuts import render, get_object_or_404
from .models import Baset, Radio, Menshawy,Husary
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

def minshview(request):
    sounds= Menshawy.objects.all()
    context={
        'title':'محمد صديق المنشاوي',
        'sounds': sounds,
    }
    return render(request,'app/menshawy.html', context)

def minshawy_play(request, sound_id):
    track= get_object_or_404(Menshawy, pk=sound_id)
    context={
        'title':'تشغيل المنشاوي',
        'track': track,
    }
    return render(request,'app/minshawyplay.html', context)

def husaryview(request):
    sounds= Baset.objects.all()
    context={
        'title':'محمود خليل الحصري',
        'sounds':sounds,
        
    }
    return render(request, 'app/husary.html', context)

def husary_play(request, sound_id):
    track= get_object_or_404(Husary, pk=sound_id)
    context={
        'title':'تشغيل الحصري',
        'track': track,
    }
    return render(request,'app/husaryplay.html', context)