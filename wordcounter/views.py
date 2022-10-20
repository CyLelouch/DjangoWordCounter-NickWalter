from ast import operator
from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    return render(request, 'homePage.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()


    worddic = {}

    for word in wordlist:
        if word in worddic:
            worddic[word] += 1
        else:
            #add to dic
            worddic[word] = 1

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'worddic':worddic})