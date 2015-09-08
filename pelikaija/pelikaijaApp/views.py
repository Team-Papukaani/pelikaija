from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', {"message":""})

def upload(request):
    if request.method == 'POST' :
        file = request.FILES['file']
        print(file.read())
        return render(request, 'index.html',{"message":"Lataus onnistui! "})
    else:
        return redirect(index)
