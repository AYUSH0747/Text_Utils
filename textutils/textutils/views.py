from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Upper Case', 'analyzed_text':analyzed}
        djtext = analyzed

    if(newlineremover=='on'):
        analyzed=''
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Line', 'analyzed_text':analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == ' '):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed


    if (charcounter == 'on'):
        count = 0
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " "):
                count += 1
                analyzed = count

        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
    if(removepunc != "on" and fullcaps!='on' and newlineremover !='on' and extraspaceremover != 'on' and charcounter != 'on'):
        return HttpResponse("Please select at least one operation and try again!")


    return render(request, 'analyze.html', params)


def contactus(request):

    return render(request, 'contactus.html')

def underconstruction(request):

    return render(request, 'underconstruction.html')



