from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import csvReader
import pandas as pd
import csv


# Create your views here.

def anasayfaView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse('denemetest')
    return render(request, "home.html", {})


def homePageView(request, *args, **kwargs):
    return HttpResponse("hd")


def getSearch(request, get_text=None):
    if request.method == "POST":
        get_text = request.POST['textfield']
        print("ife girdim")
        print("ife girmedim")
        csvReader.searchForItem(get_text)
        df = pd.read_csv("D:\\Projects\\pythonProject\\pcw\\files\\n11_search_results.csv")
        html = df.to_html()

        return render(request, "results.html", {'html': html})

    else:
        return render(request, "home.html")
