from django.shortcuts import render, redirect
import model


def test(request):
    if request.method == 'POST':
        if request.POST['strona']=='test':
            return render(request, 'learn.html', {'list': [i for i in range(20)], 'index':"", 'error': 'Podaj index zanim wyślesz dane!'})
        else:
            l = request.POST['val']
            if l != "":
                xx = []
                yy = []
                for el in l.split(','):
                    x,y = el.split('_')
                    xx.append(int(x))
                    yy.append(int(y))
            for y in yy:
                xx.append(y)
            
            for _ in range(800-len(xx)):
                xx.append(0)            
            return render(request, 'test.html',{'list': [i for i in range(20)], 'error':model.predict([xx])})
    else:
        return render(request, 'test.html',{'list': [i for i in range(20)], 'error':""})
    
def home(request):
    if request.method == 'POST':
        if request.POST['strona'] == 'test':
            return redirect('test')
        elif request.POST['strona'] == 'nauka':
            model.train()
            return render(request, 'learn.html', {'list': [i for i in range(20)], 'index':"", 'error': 'Podaj index zanim wyślesz dane!'})
        else:
            ind=request.POST['index']
            if ind!="":
                l = request.POST['val']
                if l != "":
                    xx = []
                    yy = []
                    for el in l.split(','):
                        x,y = el.split('_')
                        xx.append(int(x))
                        yy.append(int(y))
                    model.insert_data((str(xx),str(yy),int(ind)))
                return render(request, 'learn.html', {'list': [i for i in range(20)], 'error': 'Index teraz to: '+ind, 'index':ind})
            else:
                ind = request.POST['index2']
                if ind!="":
                    l = request.POST['val']
                    if l != "":
                        xx = []
                        yy = []
                        for el in l.split(','):
                            x,y = el.split('_')
                            xx.append(int(x))
                            yy.append(int(y))
                        model.insert_data((str(xx),str(yy),int(ind)))
                    return render(request, 'learn.html', {'list': [i for i in range(20)], 'error': 'Index teraz to: '+ind, 'index':ind})
                else: 
                    return render(request, 'learn.html', {'list': [i for i in range(20)], 'error': 'Nie podano indexu!', 'index':""})
    else:
        return render(request, 'learn.html', {'list': [i for i in range(20)], 'index':"", 'error': 'Podaj index zanim wyślesz dane!'})
