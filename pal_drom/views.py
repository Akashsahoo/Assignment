from django.shortcuts import render,HttpResponse

def paldrom(request):
    if request.method=='GET':
        return render(request,'paldrom.html',{})
    elif request.method=='POST':
        string=str(request.POST['paldrom'])
        print(string)

        if(ispalendrom(string) is True) :
            print(ispalendrom(string))
            return render(request, 'paldrom.html', {'msg':'string is palendrom','boolmsg':True})
        else:
            return render(request, 'paldrom.html', {'msg': 'string is not palendrom','boolmsg':True})


def index(request):
    return render(request,'index.html')


def ispalendrom(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True