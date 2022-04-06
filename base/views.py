from django.http import JsonResponse
from django.shortcuts import render
from .models import Contact
import requests

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

    for i,j,k,p in zip(ecname, edname, esdate, eedate):
        subdict={
            'ecname': i,
            'edname': j,
            'esdate': k,
            'eedate': p
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

    print("Hello data is recieved")


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

def enhance(request):
    obj = request.POST.get('obj')
    print(obj)
    API_URL = "https://api-inference.huggingface.co/models/tuner007/pegasus_paraphrase"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": obj,
        "parameters":{"min_length":10,"max_length":1000}
    })
    return JsonResponse({'cobj':output})

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