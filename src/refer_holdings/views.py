from django.shortcuts import render

# Create your views here.

def catalogues(request):
    ctx = {
        'series' :
        'author' :
        ''
    }
    return render(request, template_name = "cat_list.html", context = ctx)