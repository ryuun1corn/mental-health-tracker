from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306215160',
        'name': 'Yudayana Arif Prasojo',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
