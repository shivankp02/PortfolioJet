from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
import pickle
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.corpus import wordnet
import json
from potfolioject.settings import BASE_DIR
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def details(request):

    cname=[x for x in request.POST.getlist('cname')]
    uname=[x for x in request.POST.getlist('uname')]
    sdate=[x for x in request.POST.getlist('sdate')]
    edate=[x for x in request.POST.getlist('edate')]

    lang=[x for x in request.POST.getlist('lang')]
    slang=[x for x in request.POST.getlist('slang')]

    skill=[x for x in request.POST.getlist('skill')]
    skillnum=[x for x in request.POST.getlist('skillnum')]

    ecname=[x for x in request.POST.getlist('ecname')]
    edname=[x for x in request.POST.getlist('edname')]
    esdate=[x for x in request.POST.getlist('esdate')]
    eedate=[x for x in request.POST.getlist('eedate')]
    exp=[x for x in request.POST.getlist('exp')]

    inter =[x for x in request.POST.getlist('inter')]

    edulist=[]
    langlist=[]
    skillist=[]
    explist=[]
    intlist=[]
    for i,j,k,p in zip(cname, uname, sdate, edate):
        subdict={
            'cname': i,
            'uname': j,
            'sdate': k,
            'edate': p
        }
        edulist.append(subdict)

    for i,j,k,p,q in zip(ecname, edname, esdate, eedate, exp):
        subdict={
            'ecname': i,
            'edname': j,
            'esdate': k,
            'eedate': p,
            'exp': q
        }
        explist.append(subdict)

    for i,j in zip(lang, slang):
        subdict={
            'lang': i,
            'slang': j   
        }
        langlist.append(subdict)

    for i,j in zip(skill, skillnum):
        subdict={
            'skill': i,
            'skillnum': j
        }
        skillist.append(subdict)


    for i in inter:
        subdict={
            'inter': i
        }
        intlist.append(subdict)


    data = {
        "name":request.POST.get("name"),
        "prof":request.POST.get("prof"),
        "phone":request.POST.get("phone"),
        "email":request.POST.get("email"),
        "git":request.POST.get("git"),
        "lid":request.POST.get("lid"),
        "addr":request.POST.get("addr"),

        "Education":edulist,

        "Language":langlist,

        "careerobj":request.POST.get("careerobj"),

        "Experience": explist,

        "skills":skillist,

        "Interest":intlist
    }
    print(data)
    return render(request, 'template.html', data)

def template(request):
    return render(request,"template.html")

@csrf_exempt
def enhance(request):
    obj=str(request.POST.get("  obj"))
    lis=obj.split()
    with open(os.path.join(BASE_DIR,'base\\mlfiles\\grammer.pkl'),'rb') as file:
        data=pickle.load(file)
    lit1=[x for x in lis if x not in data['adverb'].tolist()]
    lit2=[x for x in lit1 if x not in data['noun'].tolist()]
    lit3=[x for x in lit2 if x not in STOP_WORDS]
    lit3=list(set(lit3))
    str2=" ".join([x for x in lit3])
    nlp=spacy.load('en_core_web_sm')
    str2=nlp(str2)
    l={}
    for i in range(len(lit3)):
        syno=[]
        pos=str2[i].pos_
        if pos[0].lower()=='n' or pos[0].lower()=='v' or pos[0].lower()=='a' or pos[0].lower()=='r':
            for syn in wordnet.synsets(str2[i].text,pos=pos[0].lower()):
                for lemas in syn.lemmas():
                    syno.append(lemas.name())
            if len(syno)!=0:
                syno_set=set(syno)
                syno=list(syno_set)
                if len(syno)<4:
                    l[lit3[i]]=syno
                else:
                    l[lit3[i]]=syno[0:5]
    return HttpResponse(json.dumps(l))

def contact(request):
    if request.method == 'POST':
        
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            text=request.POST.get('text')
        )
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')